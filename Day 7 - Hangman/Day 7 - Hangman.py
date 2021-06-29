import random 
import hangman_art
from hangman_words import word_list

print(hangman_art.logo)
lives=6
chosen_word=random.choice(word_list)

display=['_']*len(chosen_word)
print(''.join(display))
print(hangman_art.stages[lives])
guessed=[]
while '_' in display and lives >0:
    guess=input("What letter you want to guess?\n").lower()
    if guess in guessed:
        print(f'You have already entered the letter "{guess}", try something else!')
        continue
    else:
        guessed.append(guess)
    idx=0
    for letter in chosen_word:
        if guess==letter:
            display[idx]=guess
        idx+=1
    if guess not in chosen_word:
        lives-=1
        print(f'The letter "{guess}" is not in the word, You have "{lives}" lives left!')    
    print(''.join(display))
    print(hangman_art.stages[lives])
if not '_' in display:
    print("YOU WIN!")
if lives==0:
    print('YOU LOSE!')