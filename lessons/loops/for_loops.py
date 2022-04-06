# For loops are used to iterate over a collection
def shopping_cart():
    print("\nShopping cart example:\n")
    prices = [10, 20, 30]
    total = 0
    for item in prices:
        total += item
    
    print(f"The total for today is: ${total}")

def main():
    print("\nFor loops:\n")

    list1 = ["Mosh", "John", "Sarah"]
    list2 = [1, 2, 3, 4]

    print()
    # can iterate thru strings
    for item in list1:
        print(item)

    print()
    # can iterate thru ints
    for item in list2:
        print(item)

    print()
    # can iterate thru a range
    for item in range(10):
        print(item)

    print()
    # can iterate thru a range
    for item in range(5, 10, 2):
        print(item)

    shopping_cart()

if __name__ == '__main__':
    main()
    
    