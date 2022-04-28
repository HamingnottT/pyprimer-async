def main():
    has_high_income = True
    has_good_credit = True
    has_criminal_record = False

    # logical operators example
        # can also use & and | 
        # meets either criteria
    if has_high_income or has_good_credit:
        print("Eligible for loan")

        # meets both criteria
    if has_high_income and has_good_credit:
        print("Eligible for loan")

        # meets one criteria exclusive to the other
    if has_high_income and not has_criminal_record:
        print("Eligible for loan")

    # comparison operators
        # ==, !=, >=, <=, >, <,
    
    name = input("What is your name?: ")

    if len(name) < 3:
        print("Name must be at least 3 char long")
    elif len(name) > 50:
        print("Name cannot exceed 50 characters")
    else:
        print("Name looks good!")

if __name__ == '__main__':
    main()