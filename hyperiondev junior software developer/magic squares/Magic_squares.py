# This function checks if the given number is a positive odd integer
def is_positive_odd(n):
    return n % 2 != 0 and n > 0

# This function builds a magic square of size n x n
def create_magic_square(n):

    # Creating a 2D list of size n x n and initializing all values to 0
    magic_square = [[0 for x in range(n)] for y in range(n)]

    # Initializing position of 1
    row_index = n//2
    col_index = n-1

    # Filling the magic square with numbers
    num = 1
    while num <= n**2:
        if row_index == -1 and col_index == n:
            col_index = n-2
            row_index = 0
        else:
            if col_index == n:
                col_index = 0
            if row_index < 0:
                row_index = n-1

        if magic_square[row_index][col_index]:
            col_index -= 2
            row_index += 1
            continue
        else:
            magic_square[row_index][col_index] = num
            num += 1

        col_index += 1
        row_index -= 1

    # Returning the completed magic square
    return magic_square

# Getting input from user
while True:
    user_input = input("Enter a positive odd integer for N or 'e' to exit: ")
    
    # Exiting program if user enters 'e'
    if user_input == 'e':
        break
    
    # Converting user input to integer
    try:
        n = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a positive odd integer for N.")
        continue

    # Checking to see if the input is valid, prompt the user to enter another value if it is not
    if not is_positive_odd(n):
        print("Invalid input. Please enter a positive odd integer for N.")
        continue

    # Creating magic square
    magic_square = create_magic_square(n)

    # Printing magic square
    print("The magic square for N = ", n, " is: ")
    for row in magic_square:
        print(" ".join([str(elem) for elem in row]))

    # Verifying magic square
    row_sum = sum(magic_square[0])
    diag1_sum = 0
    diag2_sum = 0
    for i in range(n):
        # Checking row sum
        if sum(magic_square[i]) != row_sum:
            print("Incorrect")
            break
        # Checking column sum
        if sum([row[i] for row in magic_square]) != row_sum:
            print("Incorrect")
            break
        # Calculating diagonal sums
        diag1_sum += magic_square[i][i]
        diag2_sum += magic_square[i][n-i-1]
    else:
        # Checking diagonal sums
        if diag1_sum != row_sum or diag2_sum != row_sum:
            print("Incorrect")
        else:
            print("The magic square is correct!")
