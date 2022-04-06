import random as r

def main():
    tries = 3
    random_val = r.randint(1, 10)
    while tries != 0:
        guess = int(input("Pick a number between 1 and 10: "))
        if guess == random_val:
            print(f"\nYou Won! With tries left = {tries}")
            break
        else:
            tries -= 1
            if tries != 0:
                print("\nSorry, try again!")
                print(f"Tries left = {tries}")
            else:
                break

    if tries == 0:
        print("\nSorry you failed!")

    print("\nThank you for playing!")
    

if __name__ == '__main__':
    main()