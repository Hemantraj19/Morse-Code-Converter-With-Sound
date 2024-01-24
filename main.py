from morse import MORSE_CODE_DICT
import pygame
import time


def text_input():
    return input("Enter your text to convert it to morse code: ").upper()


def morse_input():
    return input("Enter your morse code to decode: ")


def text_to_morse(text):
    morse_coded_list = [MORSE_CODE_DICT[char] for char in text]
    morse_coded_text = ' '.join(morse_coded_list)
    return morse_coded_text, morse_coded_list


def morse_to_text(morse_text):
    original_text = ""
    morse_text_list = morse_text.split()
    for morse in morse_text_list:
        original_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse)]
    return original_text


def play_morse_code_sound(morse_code_list):
    pygame.init()
    dot_sound = pygame.mixer.Sound('dot.wav')
    dash_sound = pygame.mixer.Sound('dash.wav')
    for letter in morse_code_list:
        for code in letter:
            if code == '.':
                dot_sound.play()
                pygame.time.delay(int(dot_sound.get_length() * 250))
            elif code == '-':
                dash_sound.play()
                pygame.time.delay(int(dash_sound.get_length() * 250))
            # time.sleep(0.25)
        time.sleep(0.5)


# morse_to_text("- .... .. ... / .. ... / .- -. / . -..- .- -- .--. .-.. . / ... - .-. .. -. --. .-.-.-")

if __name__ == "__main__":
    print("Welcome!")
    while True:
        print("Enter 1 to encode your message\n Enter 2 to decode\nEnter 3 to exit")
        choice = input("Enter choice: ")
        if choice == '1':
            morse_code_text, morse_code_list = text_to_morse(text_input())
            print("Morse code: ", morse_code_text)
            play_sound = input("Do you want to play morse code sound (yes/no): ")
            if play_sound == 'yes':
                play_morse_code_sound(morse_code_list)
        elif choice == '2':
            print(morse_to_text(morse_input()))
        elif choice == '3':
            exit()
        else:
            print("Wrong choice, try again")
