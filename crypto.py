import re


def encrypt(original_character, key):
    original_code = ord(original_character)
    if original_code + key > 126:
        encrypted_code = ((original_code + key) - 127) + 32
    else:
        encrypted_code = original_code + key
    return chr(encrypted_code)


def decrypt(encrypted_char, key):
    encrypted_code = ord(encrypted_char)
    if encrypted_code - key < 32:
        original_code = encrypted_code + 127 - 32 - key
    else:
        original_code = encrypted_code - key
    return chr(original_code)


input_string = input("encrypted message: ")
option = input("encrypt or decrypt (e for encrypt, d for decrypt): ").lower()
option_valid = 0
while option_valid == 0:
    option_valid = 1
    if option == "e":
        key = 0
        key_valid = 0
        while key_valid == 0:
            key = input("enter key: ")
            if re.search("[^0-9]", key) == 1:
                print("invalid key!")
            else:
                key_valid = 1
                key = int(key)
        output_string = ""
        for character in input_string:
            output_string = output_string + encrypt(character, key)
        print("encrypted message: \n{output}".format(output=output_string))
    elif option == "d":
        print("outputting 100 possible decryption combinations:")
        for key in range(1, 101):
            output_string = ""
            for char in input_string:
                output_string = output_string + decrypt(char, key)
            print("Key: {key} | output: {output}".format(key=key, output=output_string))
    else:
        print("invalid option")
        option_valid = 0
