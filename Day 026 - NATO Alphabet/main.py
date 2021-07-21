import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

dic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input('Enter a word: ').upper()
nato = [dic[letter] for letter in word]
print(nato)
