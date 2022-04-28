from tempfile import TemporaryFile


def main():

    # try-except block to mitigate errors and exceptions
    try:
        pass
    except:
        pass
    finally:
        pass

    try:
        age = int(input("Age: "))
        income = 20000
        risk = income / age
        print(age)
    except ValueError:
        print("Invalid value")
    except ZeroDivisionError:
        print("Age cannot be zero")
    finally:
        pass

if __name__ == '__main__':
    main()