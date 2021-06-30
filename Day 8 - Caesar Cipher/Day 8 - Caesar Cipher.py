import art


def caesar(text, shift, direction):
    if direction != 'encode' and direction != 'decode':
        print("INVALID INPUT!")
    else:
        newWord = ''
        for i in range(len(text)):
            if text[i] not in alphabet:
                newWord += text[i]
                continue
            if direction == 'encode':
                newShift = shift-(26-alphabet.index(text[i]))
            elif direction == 'decode':
                newShift = alphabet.index(text[i])-shift
            newWord += alphabet[newShift]
        print(f'Your {direction}d word is "{newWord}".')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
on = True
while on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    ans = input(
        "Type 'yes' if you want to go again, Otherwise type 'no':\n").lower()
    if ans == 'no':
        on = False
        print("Goodbye ♥")
