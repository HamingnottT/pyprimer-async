def temperature():
    print()
    is_hot = False
    is_cold = False

    # for true if statements you can shorten 'if is_hot == True' to just 'if is_hot'
    if is_hot:
        print("It's a hot day")
        print("Drink plenty of water")
    elif is_cold:
        print("It's a cold day")
        print("Wear warm clothes")
    else:
        print("It's a lovely day")
    print("Enjoy your day")

def mortgage():
    print()
    house_price = 1000000
    down_10 = house_price * 0.10
    down_20 = house_price * 0.20

    good_credit = False
    
    if good_credit:
        print("You need to put down 10%")
        print(f"This will be your down payment: {down_10}")

    else:
        print("You need to put down 20%")
        print(f"This will be your down payment: {down_20}")

def main():
    temperature()
    mortgage()

if __name__ == '__main__':
    main()