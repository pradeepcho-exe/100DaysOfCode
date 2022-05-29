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

import random as rd

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
if user == 0:
  print(rock)
elif user == 1:
  print(paper)
else:
  print(scissors)

sys = rd.randint(0,2)
if sys == 0:
  print(f"Computer Chose:\n{rock}")
elif sys == 1:
  print(f"Computer Chose:\n{paper}")
else:
  print(f"Computer Chose:\n{scissors}")

if user == 0:
  if sys == 1:
    print("You lose")
  elif sys == 2:
    print("You win")
  else:
    print("It's draw")

elif user == 1:
  if sys == 2 :
    print("You lose")
  elif sys == 0:
    print("You win")
  else:
    print("It's draw")  
  
else:
  if sys == 0 :
    print("You lose")
  elif sys == 1:
    print("You win")
  else:
    print("It's draw")  

