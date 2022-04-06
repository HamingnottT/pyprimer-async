# 2D lists
    # these are particularly important in data science and ML
def two_d_lists():
    # when given something like a matrix like
    """
    [
        1 2 3
        4 5 6
        7 8 9
    ]
    """
    # 3 x 3 -> 3 rows 3 columns
    # we can model this matrix in a 2D list

    matrix = [
        [1, 2, 3],  # matrix[0]
        [4, 5, 6],  # matrix[1]
        [7, 8, 9]   # matrix[2]
    ]

    # we can access a number in this 2D list matrix by this syntax:
        # in matrix[0][1], the first index [0] is the row and the second index [1] is the column
    print(matrix[0][1])
    print("\n")
    # changing the value of a matrix number
    matrix[0][1] = 20
    print(matrix[0][1])
    print("\n")

    # output:
    """
    matrix = [
        [1, 20, 3], # matrix[0]
        [4, 5, 6],  # matrix[1]
        [7, 8, 9]   # matrix[2]
    ]
    """
    # using nested loops to iterate over a matrix
        
        # the first for loop will iterate over the rows
        # an inner loop will iterate over the items in that row
    for row in matrix:
        for item in row:
            print(item)

def main():
    two_d_lists()

if __name__ == '__main__':
    main()