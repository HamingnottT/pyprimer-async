def main():
    print("\narithmetic_ops started. . .")

    print("\ndivision")
        # adding an extra '/' rounds the result to int type
    print(10 / 3)
    print(10 // 3)

    print("\nmultiplication")
        # adding an extra "*" raises the first operand to the power of 'n'
    print(10 * 3)
    print(10 ** 3)

    print("\naugmented operators")
    x = 10
    print(f"initial value of x: {x}")
    x += 3
    print(x)
    x -= 3
    print(x)
    x *= 3
    print(x)

    print("\nmath functions")
    x = 2.9
    round(x)
    abs(-2.9)   #absolute value

    print("\nmath library functions")
    import math #goes at the top but for these notes I placed here for demo of importance
    x = 2.9
    
    print("\n",
    math.ceil(x), "\n",
    math.floor(x)
    )

if __name__ == '__main__':
    main()