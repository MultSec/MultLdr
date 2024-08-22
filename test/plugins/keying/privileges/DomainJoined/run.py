def desc():
    return "Check if target is Domain Joined"

def run():
    libs = '''\
#include <lm.h>
'''

    functions = '''\
//Check if domain joined
int isPartofDomain() {
    NET_API_STATUS nas;
    NETSETUP_JOIN_STATUS status;
    LPWSTR buf = NULL;
    nas = NetGetJoinInformation(NULL, &buf, &status);

    return ((nas == NERR_Success) && (status == NetSetupDomain));
}
'''

    keying = '''\
	if (!isPartofDomain())
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

    clibs = '-lnetapi32'

    # Open the file in read mode
    with open("./makefile", 'r') as file:
        content = file.read()
    
    # Replace the template
    modified_content = content.replace("{{CLIBS}}", clibs + " {{CLIBS}}")

    # Open the file in write mode and write the modified content
    with open("./makefile", 'w') as file:
        file.write(modified_content)

    return