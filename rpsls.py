import random

GAME_TEXT = ("\n\n\n\n\n\n\n\n\
        ******************************\n\n\
                    It's very simple,\n\
                    Scissors cuts paper,\n\
                    Paper covers rock,\n\
                    Rock crushes lizard,\n\
                    Lizard poisons Spock,\n\
                    Spock smashes scissors,\n\
                    Scissors decapitates lizard,\n\
                    Lizard eats paper,\n\
                    Paper disproves Spock,\n\
                    Spock vaporizes rock,\n\
                    And as it always has been,\n\
                    Rock crushes scissors.\
                    \n\n******************************\n\n\
        Pick your choice of -- Rock, Paper, Scissors, Lizard, Spock!\n\n>>>"
        )

def number_to_name(number):
    num_to_name = {0:'rock',1:'spock',2:'paper',3:'lizard',4:'scissors'}
    return num_to_name[number]


def name_to_number(name):
    name_to_num = {'rock':0,'spock':1,'paper':2,'lizard':3,'scissors':4}
    if name in name_to_num.keys():
        return name_to_num[name]
    else:
        print("Please choose one of the correct choices listed.")
        rpsls(input(GAME_TEXT).lower())

def rpsls(guess):
    print("Player's Choice >> ", guess)
    player_guess = name_to_number(guess)
    print(player_guess)
    computer_guess = random.randrange(0, 5)
    print("Computer's Choice >>", number_to_name(computer_guess))
    
    win_loss = {
            0:{'wins':[3,4],'loss':[1,2],'tie':0},
            1:{'wins':[0,4],'loss':[1,2],'tie':1},
            2:{'wins':[0,1],'loss':[2,3],'tie':2},
            3:{'wins':[2,1],'loss':[0,4],'tie':3},
            4:{'wins':[2,3],'loss':[0,1],'tie':4}
        }

    if player_guess in win_loss[computer_guess]['loss']:
        print('player wins')
    elif player_guess in win_loss[computer_guess]['wins']:
        print('player losses')
    elif player_guess == computer_guess:
        print('tie')



rpsls(input(GAME_TEXT).lower())

# rpsls("Spock")
# rpsls("paper")
# rpsls("lizard")
# rpsls("scissors")
# rpsls("rock")
