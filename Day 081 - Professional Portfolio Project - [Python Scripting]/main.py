from art import welcome

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?', "'", '!', '/', '(', ')',
           '&', ':', ';', '=', '+', '-', '_', '"', '$', '@', ' ']

morse_code_signals = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
                      '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----',
                      '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-.-.-',
                      '--..--', '..--..', '.----.', '-.-.--', '-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.',
                      '-...-', '.-.-.', '-....-', '..--.-', '.-..-.', '...-..-', '.--.-.', '/']

morse_dict = dict(zip(letters, morse_code_signals))

print(welcome)

s = input('Enter Text you want to convert to morse code: \n').lower()

answer = ''
errors = []

for letter in s:
    if letter not in morse_dict:
        errors.append(letter)
    else:
        answer += (morse_dict[letter] + ' ')

print(f'Your Morse Code is: {answer}')
if len(errors) != 0:
    print(f"The app couldn't translate these letters: \n {errors}")
