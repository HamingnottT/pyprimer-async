def basic_example():
    i = 0

    while i <= 5:
        print(i)
        i += 1
    print("Done")

    i = 0
    while i <= 5:
        print("*" * i)
        i += 1
    print("Done")

def main():
    print("\nWhile loops:\n")

    basic_example()  

if __name__ == '__main__':
    main()
    