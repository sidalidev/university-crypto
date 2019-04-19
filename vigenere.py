import utils

ALPHABET = utils.ALPHABET


def encrypt(message, key):
    message = utils.format_text(message)
    key = utils.format_text(key)
    lg = int(len(message)/len(key))+1
    cpt = 0
    new_key = ""
    while(cpt <= lg):
        new_key = new_key+key
        cpt = cpt+1

    word_translate = []
    for i in range(len(message)):
        letter_place = ALPHABET.index(message[i])+1
        word_translate.append(letter_place)

    key_translate = []
    for i in range(len(new_key)):
        letter_place_key = ALPHABET.index(new_key[i])
        key_translate.append(letter_place_key)

    addition = []
    for i in range(len(word_translate)):
        add = word_translate[i]+key_translate[i]
        if add > 25:
            add = add-26
        addition.append(add)

    encrypted_message = ""
    for i in addition:
        encrypted_message = encrypted_message+ALPHABET[i-1]
    return encrypted_message.upper()


def decrypt(encrypted_message, key):
    encrypted_message = utils.format_text(encrypted_message)
    key = utils.format_text(key)

    lg = int(len(encrypted_message)/len(key))+1
    count_key_rep = 0
    new_key = ""
    while(count_key_rep <= lg):
        new_key = new_key+key
        count_key_rep = count_key_rep+1

    word_translate = []
    for i in range(len(encrypted_message)):
        letter_place = ALPHABET.index(encrypted_message[i])+1
        word_translate.append(letter_place)

    key_translate = []
    for i in range(len(new_key)):
        letter_place_key = ALPHABET.index(new_key[i])+1
        key_translate.append(letter_place_key)

    substraction = []
    for i in range(len(word_translate)):
        sou = word_translate[i]-key_translate[i]
        substraction.append(sou)

    decrypted_message = ""
    for i in substraction:
        decrypted_message = decrypted_message+ALPHABET[i]
    return(decrypted_message.upper())
