def desc():
    return "Check if executable name is a digest to detect sanboxes"

def run():
    libs = '''\
#include <string.h>

#define MAX_DIGITS_NUM 3
'''

    functions = '''\
int CheckDigestName() {
    char buffer[MAX_PATH];
    DWORD   dwNumberOfDigits	= NULL;

    // Get path of executable
    GetModuleFileNameA(NULL, buffer, MAX_PATH);

    // Extracting just the file name from the path
    char *fileName = strrchr(buffer, '\\\\');
    if (fileName != NULL) {
        fileName++; // Move past the backslash
    } else {
        fileName = buffer; // If no backslash found, use the entire path
    }

    // Count number of digits in the executable name
	for (int i = 0; i < lstrlenA(fileName); i++){
		if (isdigit(fileName[i]))
			dwNumberOfDigits++;
	}

    // Check if the file name has more digits than the minimum allowed
    return (dwNumberOfDigits > MAX_DIGITS_NUM);
}
'''

    keying = '''\
	if (CheckDigestName())
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