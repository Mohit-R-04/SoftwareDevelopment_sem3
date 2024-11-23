# Encrypt function that wraps within the ASCII range (0-127)
def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        text = file.read()
    encrypted_text = ''.join(
        chr((ord(char) + shift) % 128) for char in text
    )
    with open(output_file, 'w') as file:
        file.write(encrypted_text)

# Decrypt function that reverses the shift and handles potential negatives
def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()
    decrypted_text = ''.join(
        chr((ord(char) - shift + 128) % 128) for char in encrypted_text
    )
    with open(output_file, 'w') as file:
        file.write(decrypted_text)
