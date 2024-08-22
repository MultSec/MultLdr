def desc():
    return "Check CPU specifications to detect sanboxes"

def run():
    libs = '''\
#define MIN_PROCS 2
'''

    functions = '''\
//Check for Computer Number of Processors
int checkProcNum() {
	SYSTEM_INFO   SysInfo   = { 0 };
	
	GetSystemInfo(&SysInfo);

	return (SysInfo.dwNumberOfProcessors <= MIN_PROCS);
}
'''

    keying = '''\
	if (checkProcNum())
		SafeEnv = FALSE;\
'''

    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{LIBS}}", libs + "\n{{LIBS}}") \
                              .replace("{{FUNCTIONS}}", functions + "\n{{FUNCTIONS}}") \
                              .replace("{{KEYING}}", keying + "\n{{KEYING}}")

    # Write the modified content to the output file
    with open("./src/main.c", 'w') as file:
        file.write(modified_content)

    return