def desc():
    return "Check if executable name changed to detect sanboxes"

def run():
    libs = '''\
#include <string.h>

#define ORIGINAL_NAME "result.exe"
'''

    functions = '''\
int CheckNameChange() {
    char buffer[MAX_PATH];

    // Get path of executable
    GetModuleFileNameA(NULL, buffer, MAX_PATH);

    // Extracting just the file name from the path
    char *fileName = strrchr(buffer, '\\\\');
    if (fileName != NULL) {
        fileName++; // Move past the backslash
    } else {
        fileName = buffer; // If no backslash found, use the entire path
    }

    // Check if the file name matches the original name
    return strcmp(fileName, ORIGINAL_NAME);
}
'''

    keying = '''\
	if (CheckNameChange())
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