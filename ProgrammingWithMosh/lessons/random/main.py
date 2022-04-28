import random

def example1():
    print("This example returns 3 random numbers.")

    for i in range(3):
        print(random.random())


def example2():
    # how to use random to randomly pick a value from a list
    members = ['John', 'Mary', 'Bob', 'Mosh']
    leader = random.choice(members)
    print(leader)

def exercise1():
    # dice role
    # attempt 1:
    dice = [1, 2, 3, 4, 5, 6]

    roll1 = random.choice(dice)
    roll2 = random.choice(dice)

    print(f"({roll1}, {roll2})")

    # /!\ needs attention
        # class method comes out with weird result
    # attempt 2:
    class Dice:
        dice = [1, 2, 3, 4, 5, 6]

        def roll(self):
            roll1 = random.choice(dice)
            roll2 = random.choice(dice)
            roll_result = (roll1, roll2)
            print(roll_result)

    print(Dice.roll)


def main():
    # example1()
    # example2()

    exercise1()
    

if __name__ == '__main__':
    main()