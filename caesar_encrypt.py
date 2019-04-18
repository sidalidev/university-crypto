import utils

ALPHABET = utils.alphabet
format_text = utils.format_text


def encrypt(message, key):
    encrypted_message = ''
    key_index = ALPHABET.find(key)
    for i in range(len(message)):
        caracter = message[i]
        location = ALPHABET.find(caracter)
        new_location = (location + key_index) % 26
        encrypted_message += ALPHABET[new_location]
    return encrypted_message.upper()


message = input("Entrez le message a crypter, exemple:  PREMIER EXEMPLE \n")
key = input("Entrez la cle, exemple: Y \n")


message = format_text(message)
key = format_text(key)

print(encrypt(message, key))
