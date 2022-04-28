def f_shape():
    print("\n")
    numbers = [5, 1, 5, 1, 1]
    for x_count in numbers:
        output = ''
        for count in range(x_count):
            output += "x"
        print(output)

    print("\n")
    numbers = [1, 1, 1, 1, 5]
    for x_count in numbers:
        output = ''
        for count in range(x_count):
            output += "x"
        print(output)

def main():

    # nested loops start from the inside for loop, 
        # then expand outward until the outermost loop is completed
    for x in range(4):
        for y in range(3):
            print(f"({x}, {y})")

    f_shape()

if __name__ == '__main__':
    main()