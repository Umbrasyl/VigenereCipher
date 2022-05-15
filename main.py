alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def key_phrase_creator(key, message):
    i = 0
    key_phrase = ""
    for letter in message:
        if letter.upper() in alphabet:
            key_phrase += key[i % len(key)]
            i += 1
        else:
            key_phrase += letter
    return key_phrase


def decoder(key, message):
    key_phrase = key_phrase_creator(key, message)
    decoded_message = ""
    for i in range(0, len(key_phrase)):
        if key_phrase[i].upper() in alphabet:
            original_index = (alphabet.index(message[i].upper()) - alphabet.index(key_phrase[i].upper())) % 26
            decoded_message += alphabet[original_index]
        else:
            decoded_message += key_phrase[i]
    return decoded_message


def encoder(key, message):
    key_phrase = key_phrase_creator(key, message)
    encoded_message = ""
    for i in range(0, len(key_phrase)):
        if key_phrase[i].upper() in alphabet:
            new_index = (alphabet.index(message[i].upper()) + alphabet.index(key_phrase[i].upper())) % 26
            encoded_message += alphabet[new_index]
        else:
            encoded_message += key_phrase[i]
    return encoded_message


his_message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
his_key = "friends"
my_message = "Hey there friend. This is Vigenere Cipher."
my_key = "cryptomessage"
my_encoded_message = encoder(my_key, my_message)
print(f"His key: {his_key}, His encoded message: {his_message}")
print(f"His message decoded: {decoder(his_key, his_message)}")
print(f"My original message: {my_message}, My key: {my_key}")
print(f"My message encoded: {my_encoded_message}")
print(f"My message decoded back: {decoder(my_key, my_encoded_message)}")
