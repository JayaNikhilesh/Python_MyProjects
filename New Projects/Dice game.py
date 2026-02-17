import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print("Must between 2 to 4 players.")
    else:
        print("Invalid,try again")

max_score = input("Enter the target score you want to compete: ")
max_score = int(max_score)
player_score = [0 for _ in range(players)]

game_over = False
while not game_over and max(player_score) < max_score:

    for player_idx in range(players):
        print("\nplayer number",player_idx + 1, "turn has just started")
        print("Your total score is: ", player_score[player_idx], "\n")
        score = 0

        while True:
            should_roll = input("Would you like to roll(y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                break
            else:
                score += value
                print("You rolled a", value)

            print("Your score is:", score)

        player_score[player_idx] += score
        print("Your total score is: ",player_score[player_idx])

        if player_score[player_idx] >= max_score:
            game_over = True

max_score = max(player_score)
winning_index = player_score.index(max_score)

print("Player number", winning_index + 1, "Is the winner with a score of:", max_score)






