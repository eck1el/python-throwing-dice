from random import shuffle

dice_numbers = [1, 2, 3, 4, 5, 6]

def throwing_dices(dice_numbers):
    dice = shuffle(dice_numbers)

    return dice_numbers[0]

def checking_play(dice1, dice2):
    if((dice1+dice2)<=6):
        print(f"The sum of the dice is {(dice1+dice2)}, unfortunate")
    elif((dice1+dice2)>6 and (dice1+dice2)<10):
        print(f"The sum of the dice is {(dice1 + dice2)} you have good chances")
    elif((dice1+dice2)>=10):
        print(f"The sum of the dice is {(dice1 + dice2)} seems like a winning move")
    else:
        pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dice1 = throwing_dices(dice_numbers)
    dice2 = throwing_dices(dice_numbers)
    print(dice1)
    print(dice2)
    checking_play(dice1, dice2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
