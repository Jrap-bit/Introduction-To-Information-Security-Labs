def caesar(inp_srt, shift):
    new_str = ""
    for i in range(len(inp_srt)):
        if inp_srt[i].isupper():
            char_shift = ord(inp_srt[i]) + shift - 65
            char_shift = (char_shift % 26)
            new_str += chr(char_shift + 65)
        elif inp_srt[i].islower():
            char_shift = ord(inp_srt[i]) + shift - 97
            char_shift = char_shift % 26
            new_str += chr(char_shift + 97)
    return new_str


def caesar_decrypt(new_str, shift):
    decrypt = ""
    for i in range(len(new_str)):
        if new_str[i].isupper():
            char_shift = ord(new_str[i]) - shift - 65
            char_shift = (char_shift % 26)
            decrypt += chr(char_shift + 65)
        elif new_str[i].islower():
            char_shift = ord(new_str[i]) - shift - 97
            char_shift = char_shift % 26
            decrypt += chr(char_shift + 97)
    return decrypt


if __name__ == "__main__":
    input_str = input("Enter the Plain Text: ")
    shift_val = int(input("Enter the Shift Value: "))
    encrypted_val = caesar(input_str, shift_val)
    print("The Cipher Text is: {}".format(encrypted_val))
    print("The Decrypted Value is: {}".format(caesar_decrypt(encrypted_val, shift_val)))
