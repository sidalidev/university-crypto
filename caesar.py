alphabet = 'ABCDEFGHIJKLMNOPKRSTUVWXYZ'


def encrypt(message, key):
    encrypted_message = ''
    for i in range(len(message)):
        caracter = message[i]
        location = alphabet.find(caracter)
        new_location = (location + key) % 26
        encrypted_message += alphabet[new_location]
    pass
    return encrypted_message


def decrypt(encrypted_message, key):
    decrypted_message = ''
    for i in range(len(encrypted_message)):
        caracter = encrypted_message[i]
        location = alphabet.find(caracter)
        new_location = (location - key) % 26
        decrypted_message += alphabet[new_location]
    pass
    return decrypted_message


print(decrypt('IFMMP', 1))
