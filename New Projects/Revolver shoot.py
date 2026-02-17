import random

def shoot():
    min_value = 1
    max_value = 6
    pull = random.randint(min_value, max_value)
    return pull

def player():
    players = [f"{player_1}", f"{player_2}"]
    chosen = random.choice(players)
    return chosen

print("Give players names: ")
player_1 = input("Name of the player 1: ")
player_2 = input("Name of the player 2: ")

pull = shoot()
chosen = player()


if chosen == player_1 :
    while pull > 0:
        print(f"The {player_1} has shot the bullet")
        pull = pull - 1

        if pull == 0:
            print(f"{player_1} is dead and {player_2} has won the game...")
            exit()

        else:
            print(f"{player_1} is still alive")
            print(f"{player_2} has shot himself")
            pull = pull - 1

            if pull == 0:
                print(f"{player_2} is dead and {player_1} has won the game...")
                exit()

            else:
                print(f"{player_2} is still alive")

else:
    while pull > 0:
        print(f"The {player_2} has shot the bullet ")
        pull = pull - 1

        if pull == 0:
            print(f"{player_2} is dead and {player_1} has won the game...")
            exit()

        else:
            print(f"{player_2} is still alive")
            print(f"{player_1} has shot himself")
            pull = pull - 1

            if pull == 0:
                print(f"{player_1} is dead and {player_2} has won the game...")
                exit()

            else:
                print(f"{player_1} is still alive")