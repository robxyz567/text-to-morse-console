from dictionary import DICTIONARY
from art import logo

print(logo)
print("Welcome to Morse code translator!\n")


def errors_message(errors):

    print("Some of the characters you entered do not appear in the Morse dictionary implemented in this program.")
    print(f"These are: {errors}. They have been replaced with the characters '?'.")


def ascii_to_morse(to_convert):

    chars_list = list(to_convert)
    morse_list = []
    errors_list = []

    for char in chars_list:
        if char == " ":
            morse_list.append("/ ")
        else:
            try:
                morse_list.append(DICTIONARY[char])
                morse_list.append(" ")
            except KeyError:
                errors_list.append(char)
                morse_list.append("? ")

    if len(errors_list) != 0:
        errors_message(errors_list)

    morse_code = "".join(morse_list)
    print(f"Your text in Morse code is: {morse_code}\n")


def morse_to_ascii(to_convert):

    ascii_list = []
    morse_list = to_convert.split()
    errors_list = []

    key_list = list(DICTIONARY.keys())
    val_list = list(DICTIONARY.values())

    for symbol in morse_list:
        if symbol in val_list:
            ascii_list.append(key_list[val_list.index(symbol)])
        elif symbol == "/":
            ascii_list.append(" ")
        else:
            ascii_list.append("?")
            errors_list.append(symbol)

    if len(errors_list) != 0:
        errors_message(errors_list)

    ascii_text = "".join(ascii_list)
    print(f"Your code in ASCII is: {ascii_text}\n")


on = True
while on:

    user_choice = input("If you want to convert ASCII to Morse, type 'm'.\n"
                        "If you want to convert Morse to ASCII type 'a'.\n"
                        "If you want to see an example, type 'e'.\n"
                        "If you want to display the ASCII-Morse dictionary, type 'd'.\n"
                        "If you want to quit the program, type 'q'.\n"
                        "Your choice: ")

    if user_choice == 'm':
        text = input("\nType text to convert: ").lower()
        ascii_to_morse(text)
    elif user_choice == 'a':
        code = input("\nType code to convert: ").lower()
        morse_to_ascii(code)
    elif user_choice == 'e':
        print("\nText in ASCII: an example")
        print("Code in Morse: .- -. / . -..- .- -- .--. .-.. .")
        print("Note that in the Morse code, words are separated by '/'.\n")
    elif user_choice == 'd':
        print(f"\nDICTIONARY: {DICTIONARY}\n")
    elif user_choice == 'q':
        on = False
    else:
        print("\nInvalid command!")






