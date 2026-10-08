import time
import winsound

MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', 
    # Turkish Characters
    'Ç': '-.-.',  'Ğ': '--.',   'İ': '..',    'Ö': '---.',  'Ş': '----',  'Ü': '..--',
    # Punctuation Marks
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.'
}

def text_to_morse():
    user_input = input("Please enter a text to convert to Morse code: ").upper()
    if user_input == "":
        print("You did not enter any text.")
        return ""

    print("\nSignals:")
    for char in user_input:
        if char == " ":
            print("/ ", end="", flush=True)  # Space between words
            time.sleep(0.3)  # Space between words
        elif char in MORSE_CODE:
            for symbol in MORSE_CODE[char]:
                print(symbol, end="", flush=True)
                if symbol == ".":
                    winsound.Beep(800,350)  # Dot: 350 ms beep
                elif symbol == "-":
                    winsound.Beep(800,850)  # Dash: 850 ms beep
                time.sleep(0.19)  # Space between symbols    

            print(" ", end="", flush=True)
            time.sleep(0.21)  # Space between letters
        else:
            print(f"\nCharacter '{char}' cannot be converted to Morse code.")
            return ""

text_to_morse()
print("\nCommunication Completed")

