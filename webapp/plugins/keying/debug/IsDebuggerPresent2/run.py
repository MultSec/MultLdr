def desc():
    return "IsDebuggerPresent Native API call"

def run():
    libs = '''\
#include <winternl.h>
'''
    keying = '''\
	if (((PEB*)(__readgsqword(0x60)))->BeingDebugged == 1)
		SafeEnv = FALSE;\
'''

    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{LIBS}}", libs + "\n{{LIBS}}") \
                              .replace("{{KEYING}}", keying + "\n{{KEYING}}")

    # Write the modified content to the output file
    with open("./src/main.c", 'w') as file:
        file.write(modified_content)

    return