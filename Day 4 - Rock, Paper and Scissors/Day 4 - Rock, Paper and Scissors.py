rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ans=input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n")
if ans=='0':
  print(rock)
elif ans=='1':
  print(paper)
else:
  print(scissors)

print("Computer chose:\n")

import random
rand=random.randint(0,2)
if rand==0:
  print(rock)
elif rand==1:
  print(paper)
else:
  print(scissors)
win='YOU WON!'
lose='YOU LOST!'
draw='DRAW!'
if ans=='0' and rand==0:
  print(draw)
elif ans=='0' and rand==1:
  print(lose)
elif ans=='0' and rand==2:
  print(win)
elif ans=='1' and rand==0:
  print(win)
elif ans=='1' and rand==1:
  print(draw)
elif ans=='1' and rand==2:
  print(lose)
elif ans=='2' and rand==0:
  print(lose)
elif ans=='2' and rand==1:
  print(win)
elif ans=='2' and rand==2:
  print(draw)
else:
  print("You typed an invalid number, {lose}")

