def main():
    print("This program can convert your weight from lbs to kilos and vice versa.")

    weight = int(input("Input your weight here: "))

    metric = input("(L)bs or (K)g: ").upper()

    pounds2kilos = round(weight/2.20462, 2) # or weight*0.45
    kilos2pounds = round(weight*2.20462, 2) # or weight/0.45

    if metric == "L":
        print(f"Your weight is {pounds2kilos} kg")
    elif metric == "K":
        print(f"Your weight is {kilos2pounds} lbs")
    else:
        print("Error: wrong input")

if __name__ == '__main__':
    main()