import utils

alphabet = utils.alphabet
format_text = utils.format_text


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


message = input("Entrez le message a decrypter, exemple:  PREMIER EXEMPLE \n")
key = input("Entrez la cle, exemple: Y \n")


message = format_text(message)
key = format_text(key)

print('Message decrypte: ', decrypt(message, key))
