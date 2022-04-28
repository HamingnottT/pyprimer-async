def duplicates():
    numbers = [5, 2, 1, 7, 4, 5, 4]
    uniques = []

    for i in numbers:
        if i not in uniques:
            uniques.append(i)

    print(numbers)
    print(uniques)

def main():
    numbers = [5, 2, 1, 7, 4]
    numbers.append(20)
    print(numbers)

    # inserts 10 to the beginning of the list
        # syntax list.insert(index, argument)
    numbers.insert(0, 10)

    # removes a particular item by its value
    numbers.remove(5)

    # clears the list
    numbers.clear()

    # deletes the last item in the list
    numbers.pop()

    # returns the first instance of value 5
    numbers.index(5)

    # check for the existance of 50
        # returns False without error
    print(50 in numbers)

    # counts the number of instances of an item value
    numbers.count(5)

    # sorts the list by its values in ascending order
        # note: this returns a none type value so to view the list simply call it again
    numbers.sort()
    print(numbers)

    # sorts the list in descending/reverse order
    numbers.reverse()

    # creates a copy of the list values stored in a new variable
    numbers2 = numbers.copy()
    numbers.append(10)


if __name__ == '__main__':
    # main()
    duplicates()
