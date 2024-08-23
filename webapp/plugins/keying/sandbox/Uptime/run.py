def desc():
    return "Check uptime to detect sanboxes"

def run():
    libs = '''\
#define MIN_UPTIME 300000 // 5 min; 5*60=300s; 5*60*1000=300000 ms
'''

    functions = '''\
//Check for Computer Uptime Greater than 5 min
int checkUptime() {
    // System uptime
    // We are using GetTickCount64
    // Retrieves the number of milliseconds that have elapsed since the system was started.
    // https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount64
    return (GetTickCount() < (MIN_UPTIME));
}
'''

    keying = '''\
	if (checkUptime())
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