import random


def d6():
    global resultD6
    resultD6 = random.randrange(1, 7)
    return resultD6


def d20():
    global resultD20
    resultD20 = random.randrange(1, 21)
    return resultD20


def d4():
    global resultD4
    resultD4 = random.randrange(1, 5)
    return resultD4


dice_value = input(
    "Please select which dice to roll - D4, D6 or D20: ").lower()
dice_sum = 0
if dice_value not in ["d4", "d6", "d20"]:
    print("Not a valid dice!")
else:
    times = int(input("How many times to roll (max 5 rolls): "))
    if times > 5:
        print("Too many rolls!")
    elif times <= 0:
        print("No dice!")
    else:
        for i in range(times):
            if dice_value == "d6":
                print(f"{i+1} roll : {d6()}")
                dice_sum += resultD6
            elif dice_value == "d20":
                print(f"{i+1} roll : {d20()}")
                dice_sum += resultD20
            elif dice_value == "d4":
                print(f"{i+1} roll : {d4()}")
                dice_sum += resultD4
        print(f"{times}{dice_value} TOTAL: {dice_sum}")
