import random

class Dice_Randomizer:

    #Prompting for the set of dice to be rolled
    type_prompt = input ("Enter the dice roll(s) in following format (#d# # of times): ")

    #Should change this to be dynamic
    dicenum_num = int(type_prompt[0])
    type_num = int(type_prompt[2])
    iter_num = int(type_prompt[4])

    rolls = []

    print ("Below are the results for rolling", dicenum_num, "d", type_num, "dice", iter_num, "times.")

    for i in range(iter_num):
        rolls.append([])
        for j in range(dicenum_num):
            rolls[i].append(random.randint(1, type_num))
    
    print (rolls)

    sum_prompt = input ("Would you like to sum the results? (Yes or No) " )

    temp = 0
    sum = []
    if sum_prompt == "Yes":
        for i in range(iter_num):
            for j in range(dicenum_num):
                temp += rolls[i][j]
            sum.append(temp)
            print (temp)
            temp = 0
        print (sum)
    else:
        print (rolls)