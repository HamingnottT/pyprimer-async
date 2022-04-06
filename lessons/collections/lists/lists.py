def basic_practice():
    names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

    # indexing
    print(names[0])
    print(names[2])
    print(names[-1])

    # slicing
    print(names[2:])
    print(names[:-2])
    print(names[::])

    # note: slicing returns new lists from the old
        # useful for working with immutables
    
    # changing the name of an index
    names[0] = input("New name: ")
    print(names)

def largest_number():
    numbers = [4, 5, 2, 7, 9]
    max = numbers[0]
    
    for i in numbers:
        if i >= max:
            max = i
    
    print(max)

def main():
    # basic_practice()
    largest_number()

if __name__ == '__main__':
    main()