import random

# Create nested lists on each Elements strenghts and weaknesses. Inside nested lists, there has to be a comma otherwise it will think it's a tuple and not a list
fire_element = [["Fire", ["Water", "Extinguishes"], ["Earth", "Burns"]]]
water_element = [["Water", ["Fire", "Extinguishes"], ["Earth", "Absorbs"]]]
earth_element = [["Earth", ["Water", "Absorbs"], ["Fire", "Burns"]]]

elements_sw = [fire_element, water_element, earth_element]

print("\nWelcome to Elements Clash Game!\n")

print("\nChoose your element\n")
print("1. Fire")
print("2. Water")
print("3. Earth\n")

# Player 1 selects a choice out of the four elements which then converts the input from a string into an integer
player1_choice = int(input("Player 1: Enter your choice (1-3): "))

# Player two makes a random choice from numbers 1 to 3 which represent 1. Fire, 2. Water, 3. Earth.
player2_choice = random.randint(1, 3)


# If player1 or player 2 selects option number 1, it's Fire which is accessible in the elements_sw nested list in array [0][0][0]
if player1_choice == 1:
    player1_choice = elements_sw[0][0][0]
elif player1_choice == 2:
    player1_choice = elements_sw[1][0][0]
elif player1_choice == 3:
    player1_choice = elements_sw[2][0][0]


if player2_choice == 1:
    player2_choice = elements_sw[0][0][0]
elif player2_choice == 2:
    player2_choice = elements_sw[1][0][0]
elif player2_choice == 3:
    player2_choice = elements_sw[2][0][0]

# Create a condition where Fire beats Water, Earth beats water and Fire beats earth

# Water wins()

if (
    player1_choice == elements_sw[0][0][0] or player2_choice == elements_sw[0][0][0]
) and (
    player1_choice == elements_sw[1][0][0] or player2_choice == elements_sw[1][0][0]
):
    print(f"\nPlayer 1 chooses: {player1_choice}\nPlayer 2 chooses: {player2_choice}\n")

    if player1_choice == elements_sw[1][0][0]:
        print("\nPlayer 1 Wins!!")
    elif player2_choice == elements_sw[1][0][0]:
        print("\nPlayer 2 Wins!!")

    print(
        f"\n{elements_sw[1][0][0]} {elements_sw[1][0][1][1]} {elements_sw[1][0][1][0]}!!!\n"
    )

# Fire wins()

elif (
    player1_choice == elements_sw[0][0][0] or player2_choice == elements_sw[0][0][0]
) and (
    player1_choice == elements_sw[2][0][0] or player2_choice == elements_sw[2][0][0]
):
    print(f"\nPlayer 1 chooses: {player1_choice}\nPlayer 2 chooses: {player2_choice}\n")

    if player1_choice == elements_sw[0][0][0]:
        print("\nPlayer 1 Wins!!")
    elif player2_choice == elements_sw[0][0][0]:
        print("\nPlayer 2 Wins!!")

    print(
        f"\n{elements_sw[0][0][0]} {elements_sw[0][0][2][1]} {elements_sw[0][0][2][0]}!!!\n"
    )


# Earth wins ()

elif (
    player1_choice == elements_sw[1][0][0] or player2_choice == elements_sw[1][0][0]
) and (
    player1_choice == elements_sw[2][0][0] or player2_choice == elements_sw[2][0][0]
):
    print(f"\nPlayer 1 chooses: {player1_choice}\nPlayer 2 chooses: {player2_choice}\n")

    if player1_choice == elements_sw[2][0][0]:
        print("\nPlayer 1 Wins!!")
    elif player2_choice == elements_sw[2][0][0]:
        print("\nPlayer 2 Wins!!")

    print(
        f"\n{elements_sw[2][0][0]} {elements_sw[2][0][1][1]} {elements_sw[2][0][1][0]}!!!\n"
    )

else:
    print("\nBoth Player 1 and Player 2 Draw!!\n")
