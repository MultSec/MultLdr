def desc():
    return "Check storage size to detect sanboxes"

def run():
    libs = '''\
#define MIN_STORAGE 100 // 100GB
'''

    functions = '''\
int checkDiskSize() {
    // Disk size
    // We are using GetDiskFreeSpaceExA
    // Retrieves information about the amount of space that is available on a disk volume,
    // which is the total amount of space, the total amount of free space, and the total
    // amount of free space available to the user that is associated with the calling thread.
    // https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getdiskfreespaceexa

    ULARGE_INTEGER iFreeBytesAvailableToCaller, iTotalNumberOfBytes, iTotalNumberOfFreeBytes;

	// Retrieve information for disk C:
    GetDiskFreeSpaceExA("C:\\\\", &iFreeBytesAvailableToCaller, &iTotalNumberOfBytes, &iTotalNumberOfFreeBytes);

    return ((iTotalNumberOfBytes.QuadPart / 1073741824) <= MIN_STORAGE);
}
'''

    keying = '''\
	if (checkDiskSize())
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