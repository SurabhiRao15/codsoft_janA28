import random
options=['Rock','Paper','Scissor']
name=input("Enter your name :")
ComputerScore=0
PlayerScore=0
NumberOfRounds=0
gameOn=True
print(f"Welcome to the game {name.title()}")
while NumberOfRounds<5:
  ComputerOption=random.choice(options)
  PlayerOption=input("Enter Rock/ Paper/ Scissor :").title()
  print(f"Computer choice :{ComputerOption}")
  print(f"{name.title()} option :{PlayerOption}")
  NumberOfRounds += 1
  if ComputerOption==PlayerOption:
    print('Oh ! It is a Tie')
  elif (ComputerOption=='Rock' and PlayerOption == 'Scissor') or (ComputerOption=='Scissor' and PlayerOption=='Paper') or (ComputerOption=='Paper' and ComputerOption=='Rock'):
    print("Yepee !! Computer wins")
    ComputerScore += 1
  elif (PlayerOption=='Rock' and ComputerOption == 'Scissor') or (PlayerOption=='Scissor' and ComputerOption=='Paper') or (PlayerOption=='Paper' and ComputerOption=='Rock'):
    print(f"Hurray !! {name.title()} wins")
    PlayerScore += 1
  else:
    print(" Oh no...Choose a valid option to play this game.")
  print("-------------------------")
  print("")
  print(f"Round No: {NumberOfRounds}")
  print("------ Score Board ------")
  print(f"{name.title()}: {PlayerScore} | Computer: {ComputerScore}")
  print("===============================")
  print("")
  if NumberOfRounds==5:
    gameOn=False
    break
if PlayerScore==ComputerScore:
  print("Draw!!")
elif PlayerScore>ComputerScore:
  print(f"Congrats {name.title()}, You won the game!!")
else:
  print(f"Oops Computer won the game!! Better luck next time {name.title()}!")
