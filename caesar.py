alphabet = 'ABCDEFGHIJKLMNOPKRSTUVWXYZ'
message = 'HELLO'
key = 1

message_length = len(message)

encrypted_message = ''

for i in range(message_length):
    caracter = message[i]
    location = alphabet.find(caracter)
    new_location = (location + key) % 26
    encrypted_message += alphabet[new_location]
    pass

print(encrypted_message)
