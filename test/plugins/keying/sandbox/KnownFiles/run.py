def desc():
    return "Check Known Files to detect sanboxes"

def run():
    libs = '''\
#include "shlwapi.h"
'''

    functions = '''\
int checkFilePaths() {
	LPCWSTR filePaths[] = {
        // VMWare
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\Vmmouse.sys",
		L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vm3dgl.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmdum.dll",
		L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vm3dver.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmtray.dll",
		L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmci.sys", 
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmusbmouse.sys",
		L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmx_svga.sys", 
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmxnet.sys",
		L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\VMToolsHook.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmhgfs.dll",
		L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmmousever.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmGuestLib.dll",
		L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\VmGuestLibJava.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\vmscsi.sys",

        // Virtual Box
		L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\VBoxMouse.sys", 
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\VBoxGuest.sys",
		L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\VBoxSF.sys", 
        L"C:\\\\windows\\\\Sysnative\\\\Drivers\\\\VBoxVideo.sys",
		L"C:\\\\windows\\\\Sysnative\\\\vboxdisp.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\vboxhook.dll",
		L"C:\\\\windows\\\\Sysnative\\\\vboxmrxnp.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\vboxogl.dll",
		L"C:\\\\windows\\\\Sysnative\\\\vboxoglarrayspu.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\vboxoglcrutil.dll",
		L"C:\\\\windows\\\\Sysnative\\\\vboxoglerrorspu.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\vboxoglfeedbackspu.dll",
		L"C:\\\\windows\\\\Sysnative\\\\vboxoglpackspu.dll", 
        L"C:\\\\windows\\\\Sysnative\\\\vboxoglpassthroughspu.dll",
		L"C:\\\\windows\\\\Sysnative\\\\vboxservice.exe", 
        L"C:\\\\windows\\\\Sysnative\\\\vboxtray.exe",
		L"C:\\\\windows\\\\Sysnative\\\\VBoxControl.exe"
    };

    // Check the presence of the paths
	for (int i=0; i < (sizeof(filePaths) / sizeof(filePaths[0])); ++i) {
		if (PathFileExists(filePaths[i]))
			return 1;
	}

    return 0;
}
'''

    keying = '''\
	if (checkFilePaths())
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

    clibs = '-lshlwapi'

    # Open the file in read mode
    with open("./makefile", 'r') as file:
        content = file.read()
    
    # Replace the template
    modified_content = content.replace("{{CLIBS}}", clibs + " {{CLIBS}}")

    # Open the file in write mode and write the modified content
    with open("./makefile", 'w') as file:
        file.write(modified_content)

    return