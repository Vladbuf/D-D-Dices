import random


def d6():
    global resultD6
    resultD6 = random.randrange(1, 7)
    if resultD6 == 6:
        print("Critical!!!")
    elif resultD6 == 1:
        print("Fail")
    return resultD6


def d20():
    global resultD20
    resultD20 = random.randrange(1, 21)
    if resultD20 == 20:
        print("Critical!!!")
    elif resultD20 == 1:
        print("Bad Luck!")
    return resultD20


def d4():
    global resultD4
    resultD4 = random.randrange(1, 5)
    if resultD4 == 4:
        print("Critical!!!")
    return resultD4


dice_value = input("🎲Please select the dice to roll - D4, D6 or D20: ").lower()
dice_sum = 0
if dice_value not in ["d4", "d6", "d20"]:
    print("Not a valid dice!")
else:
    times = int(input("How many dices: "))
    for i in range(times):
        if dice_value == "d6":
            print(d6())
            dice_sum += resultD6
        elif dice_value == "d20":
            print(d20())
            dice_sum += resultD20
        elif dice_value == "d4":
            print(d4())
            dice_sum += resultD4
    print(f"{times}{dice_value} TOTAL: {dice_sum}")
