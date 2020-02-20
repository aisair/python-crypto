import re
from spellchecker import SpellChecker
import colorama


def encrypt(original_char, encrypt_key):
    original_code = ord(original_char)
    if original_code + encrypt_key > 126:
        encrypted_code = ((original_code + encrypt_key) - 127) + 32
    else:
        encrypted_code = original_code + encrypt_key
    return chr(encrypted_code)


def decrypt(encrypted_char, encrypt_key):
    encrypted_code = ord(encrypted_char)
    if encrypted_code - encrypt_key < 32:
        original_code = encrypted_code + 127 - 32 - encrypt_key
    else:
        original_code = encrypted_code - encrypt_key
    return chr(original_code)


colorama.init()
input_string = input("input string/message: ")
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
        option = input("does your string use words from the dictionary? (y, n): ").lower()
        d = SpellChecker()
        output_array = [[], [], []]  # = [[string, ...], [key, ...], [probability (if applicable), ...]]
        for key in range(1, 95):
            output_array[0].append("")
            for char in input_string:
                output_array[0][-1] = output_array[0][-1] + (decrypt(char, key))
            output_array[1].append(key)
            if option == "y":
                c = 0
                for check_word in output_array[0][-1].split(" "):
                    if check_word in d:
                        c += 1
                output_array[2].append(c / len(output_array[0][-1].split(" ")))
        print("decryption results: ")
        if option == "y":
            max_index = output_array[2].index(max(output_array[2]))
            for index in range(len(output_array[0])):
                print("key: {key} | output: {green}{out}{reset} | probability: {chance}%".format(
                    key=output_array[1][index], out=output_array[0][index], chance=output_array[2][index] * 100,
                    green=colorama.Fore.LIGHTGREEN_EX, reset=colorama.Fore.RESET))
            print("highest probability:\nkey: {key} | output: {green}{out}{reset} | probability: {chance}%".format(
                key=output_array[1][max_index], out=output_array[0][max_index], chance=output_array[2][max_index] * 100,
                green=colorama.Fore.LIGHTGREEN_EX, reset=colorama.Fore.RESET))
        else:
            for index in range(len(output_array[0])):
                print("key: {key} | output: {green}{out}{reset}".format(key=output_array[1][index],
                                                                        out=output_array[0][index],
                                                                        green=colorama.Fore.LIGHTGREEN_EX,
                                                                        reset=colorama.Fore.RESET))
    else:
        print("invalid option")
        option_valid = 0
