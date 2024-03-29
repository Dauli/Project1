# Project of PIG Game

# In this game, everyone has a turn
# User need to enter number of players
# then each player has a turn where he has roll the dine,
# when u rolled, you got a random number from 1 to 6,
# if you get anything beside one, which mean between 2 to 6,
# you get that number you add it to your score, for example,
# you rolled 5, you get 5, then you rolled again you get 3, you score
# will be 5 + 3, and so on.
# But when you get a 1, your score wipped to a zero.


# We start by generating a radom number between 1 - 6
# Lets import the random modul
import random

# let us define a roll function roll between 1 and 6
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


# continue to ask user for a valid number of players
while True:
    players = input('Enter the number of players (1-4): ')

    # if input is a number, convert it to int
    if players.isdigit():
        players = int(players)
        if players >= 2 and players <= 4:
            break
        else:
            print("Must be between 1 - 4 players.")
    else:
        print("Invalid, try again.")


# Assimulate each players turn
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print('\nPlayer number', player_idx + 1, 'turn has just started!\n')
        current_score = 0

        while True:
            should_roll = input('Would you like to rool (y)? ')
            if should_roll.lower() != 'y':
                break
            
            # use roll() function
            value = roll()
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a:', value)

            print('Your score is:', current_score)

        player_scores[player_idx] += current_score
        print('Your total score is:', player_scores[player_idx])

# Declare the winner
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print('Player number', winning_idx + 1,
      'is the winner with a score of:', max_score)