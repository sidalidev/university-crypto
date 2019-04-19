import utils

ALPHABET = utils.ALPHABET
COMMON_LETTERS = utils.COMMON_LETTERS
format_text = utils.format_text


def encrypt(message, key):
    message = format_text(message)
    key = format_text(key)
    encrypted_message = ''
    key_index = ALPHABET.find(key)
    for i in range(len(message)):
        caracter = message[i]
        location = ALPHABET.find(caracter)
        new_location = (location + key_index) % 26
        encrypted_message += ALPHABET[new_location]
    return encrypted_message.upper()


def decrypt(encrypted_message, key=None):
    encrypted_message = format_text(encrypted_message)

    if key is None:
        key = find_key_from_encrypted_message(encrypted_message)
    else:
        key = ALPHABET.index(format_text(key))

    plain_text = ""
    for letter in encrypted_message:
        index = ALPHABET.find(letter)
        new_index = flatten(index - key)
        plain_text += ALPHABET[new_index]

    return plain_text.upper()


def flatten(number):
    return number - (26*(number//26))


def find_key_from_encrypted_message(cipher_text):
    index_of_most_common_letter = 4
    distribution_dict = analyse_letter_distribution(cipher_text)
    COMMON_LETTERS = sorted(
        distribution_dict, key=distribution_dict.get, reverse=True)
    key = ALPHABET.find(
        COMMON_LETTERS[0]) - index_of_most_common_letter
    return key


def analyse_letter_distribution(cipher_text):
    distribution_dict = {}
    for letter in cipher_text:
        if letter not in distribution_dict:
            distribution_dict[letter] = 1
        else:
            distribution_dict[letter] += 1
    return distribution_dict
