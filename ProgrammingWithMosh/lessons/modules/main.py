import numbers
from utils import find_max
    
def modules_example():

    print("\nThis function will find the maxiumum number of a list:\n")
    user_list = []
    
    user_input = input("enter list: ")
    user_input = user_input.split(" ")
    for i in user_input:
        user_list.append(int(i))
    
    result = find_max(numbers=user_list)  # call function from utils module
    
    print(f"The maximum number is {result}")


def main():
    modules_example()
    

if __name__ == '__main__':
    main()