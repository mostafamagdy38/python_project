import random

def get_choices():
    player_choice = input("Entr a choice (rock, paper, scissors): ")
    options = ['rock','paper','scissors']
    computer_choice = random.choice(options)
    choices = {"player" : player_choice , "computer" : computer_choice}
    return choices

def check_win(player, computer):
    print(f"You choose   {player},  comp Choose  {computer}")
    if player == computer:
     return "its a Tie"
    elif player == "rock":
       if computer == "scissors":
        return"player win"
    elif player == "rock":
       if computer == "Paper":
         return"computer win"
    elif player == "paper":
       if computer == "rock":
         return"player win"
    elif player == "paper":
       if computer == "scissors":
         return"computer win" 
    elif player == "scissors":
       if computer == "paper":
         return"player win"
    elif player == "scissors":
       if computer == "rock":
         return"computer win"

choices = get_choices()
result = check_win(choices["player"], choices["computer"]) 
print(result)
