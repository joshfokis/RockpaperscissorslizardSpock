import random


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        return "scissors"


def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Please choose one of the correct choices listed."
        rpsls(raw_input("\n\n\n\n\n\n\n\n\
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
        Pick your choice of -- Rock, Paper, Scissors, Lizard, Spock!\n\n>>>").lower())


def rpsls(guess):
    print "Player's Choice >> ", guess
    player_guess = name_to_number(guess)
    computer_guess = random.randrange(0, 5)
    number_to_name(computer_guess)
    print "Computer's Choice >>", number_to_name(computer_guess)

    # Rock
    if computer_guess == 0 and player_guess == 3:
        print "Computer Wins!"
    elif computer_guess == 0 and player_guess == 4:
        print "Computer Wins!"
    elif computer_guess == 0 and player_guess == 1:
        print "Player Wins!"
    elif computer_guess == 0 and player_guess == 2:
        print "Player Wins!"
    # Spock
    elif computer_guess == 1 and player_guess == 0:
        print "Computer Wins!"
    elif computer_guess == 1 and player_guess == 4:
        print "Computer Wins!"
    elif computer_guess == 1 and player_guess == 2:
        print "Player Wins!"
    elif computer_guess == 1 and player_guess == 3:
        print "Player Wins!"

    elif computer_guess == 2 and player_guess == 1:
        print "Computer Wins!"
    elif computer_guess == 2 and player_guess == 0:
        print "Computer Wins!"
    elif computer_guess == 2 and player_guess == 3:
        print "Player Wins!"
    elif computer_guess == 2 and player_guess == 4:
        print "Player Wins!"

    elif computer_guess == 3 and player_guess == 2:
        print "Computer Wins!"
    elif computer_guess == 3 and player_guess == 1:
        print "Computer Wins!"
    elif computer_guess == 3 and player_guess == 0:
        print "Player Wins!"
    elif computer_guess == 3 and player_guess == 4:
        print "Player Wins!"

    elif computer_guess == 4 and player_guess == 3:
        print "Computer Wins!"
    elif computer_guess == 4 and player_guess == 2:
        print "Computer Wins!"
    elif computer_guess == 4 and player_guess == 0:
        print "Player Wins!"
    elif computer_guess == 4 and player_guess == 1:
        print "Player Wins!"

    elif computer_guess == player_guess:
        print "It is a Tie!"

rpsls(raw_input("\n\n\n\n\n\n\n\n******************************\n\n\
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
        Pick your choice of -- Rock, Paper, Scissors, Lizard, Spock!\n\n>>>"))

# rpsls("Spock")
# rpsls("paper")
# rpsls("lizard")
# rpsls("scissors")
# rpsls("rock")
