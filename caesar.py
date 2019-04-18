alphabet = 'abcdefghijklmnopkrstuvwxyz'


def encrypt(message, key):
    encrypted_message = ''
    key_index = alphabet.find(key)
    for i in range(len(message)):
        caracter = message[i]
        location = alphabet.find(key_index)
        new_location = (location + key) % 26
        encrypted_message += alphabet[new_location]
    pass
    return encrypted_message.upper()


def decrypt(encrypted_message, key):
    decrypted_message = ''
    key_index = alphabet.find(key)
    for i in range(len(encrypted_message)):
        caracter = encrypted_message[i]
        location = alphabet.find(caracter)
        new_location = (location - key_index) % 26
        decrypted_message += alphabet[new_location]
    pass
    return decrypted_message.upper()


# print(decrypt('MZMVCVDFULCVUVTIPGKF', 'R'))

message = input('Entrez votre message: ')
key = input('Entrez votre cle: ')

message = message.lower()
key = key.lower()

print(decrypt(message, key))
