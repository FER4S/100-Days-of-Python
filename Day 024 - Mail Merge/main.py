with open('Input/Letters/starting_letter.docx') as letter:
    content = letter.read()

with open('Input/Names/invited_names.txt') as inv_names:
    names = inv_names.readlines()

for name in names:
    new_name = name.strip('\n')
    with open(f'Output/ReadyToSend/{new_name}.docx', 'w') as ready:
        new_letter = content.replace('[name]', new_name)
        ready.write(new_letter)
