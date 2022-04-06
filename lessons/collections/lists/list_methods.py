def main():
    numbers = [5, 2, 1, 7, 4]
    numbers.append(20)
    print(numbers)

    # inserts 10 to the beginning of the list
        # syntax list.insert(index, argument)
    numbers.insert(0, 10)

    numbers.remove(5)

    numbers.clear()

    numbers.pop()


if __name__ == '__main__':
    main()