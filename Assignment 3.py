# Function to add matrices
def add_matrices():
    
    # Prompt the user for the number of rows and columns
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    
    
    # Initialize two matrices with zeros
    matrix1 = []
    matrix2 = []
    # Prompt the user to enter elements for the first matrix
    print("Enter elements for the first matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix1.append(row)

    # Prompt the user to enter elements for the second matrix
    print("Enter elements for the second matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix2.append(row)

    # Add the two matrices
    result_matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            element = matrix1[i][j] + matrix2[i][j]
            row.append(element)
        result_matrix.append(row)

    # Display the result matrix
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)
        
    # Function to check rotation
    
def check_rotation():
    
    # Prompt for matrix X
    rows_x = int(input("Enter the number of rows in matrix X: "))
    cols_x = int(input("Enter the number of columns in matrix X: "))
    matrix_x = []

    print("Enter matrix X:")
    for i in range(rows_x):
        row = input().split()
        matrix_x.append(row)

    # Prompt for matrix Y
    rows_y = int(input("Enter the number of rows in matrix Y: "))
    cols_y = int(input("Enter the number of columns in matrix Y: "))
    matrix_y = []

    print("Enter matrix Y:")
    for i in range(rows_y):
        row = input().split()
        matrix_y.append(row)

    # Check rotation
    if cols_x == rows_y and rows_x == cols_y:
        rotated_x = [[matrix_x[j][i] for j in range(rows_x)] for i in range(cols_x)]
        if rotated_x == matrix_y:
            print("Matrix X is the rotation of matrix Y")
        else:
            print("Matrix X is not the rotation of matrix Y")

        print("Original matrix X:")
        for row in matrix_x:
            print(" ".join(row))

        print("Rotated matrix X:")
        for row in rotated_x:
            print(" ".join(row))
    else:
        print("Matrix X is not the rotation of matrix Y")

# Function to invert a dictionary
def invert_dictionary():
    original_dict = {}
    inverted_dict = {}

    # Input key-value pairs for the dictionary
    while True:
        key = input("Enter a key (or press Enter to finish): ")
        if not key:
            break
        value = input(f"Enter the value for key '{key}': ")

        if value in inverted_dict:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key
        original_dict[key] = value

    print("Before inverting:")
    print(original_dict)
    
    # Invert the dictionary and handle multiple keys for the same value
    inverted_dict = {}
    for key, value in original_dict.items():
        if value in inverted_dict:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key

    print("After inverting:")
    print(inverted_dict)

    # Function to convert a matrix to a dictionary

def convert_matrix_to_dictionary():
    matrix = []

    # Prompt for matrix size
    rows = int(input("Enter the number of users: "))

    # Prompt for user data
    for i in range(rows):
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        user_id = input("Enter the ID: ")
        job_title = input("Enter the job title: ")
        company = input("Enter the company: ")

        user_data = [first_name, last_name, job_title, company]
        matrix.append([user_id] + user_data)

    # Convert matrix to dictionary
    user_dict = {row[0]: row[1:] for row in matrix}
   
    user_dict = convert_matrix_to_dictionary()
    print(user_dict)

    return user_dict




    # Function to check if a string is a palindrome
def check_palindrome():
    
    # Prompt for string
    s = input("Enter a string: ")

    # Reverse the string
    reversed_s = s[::-1]

    # Display original and reversed strings
    print("Original string:", s)
    print("Reversed string:", reversed_s)

    # Check if palindrome
    if s == reversed_s:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

def search_element_and_merge_sort():
    # Function to search for an element and perform merge sort
    pass
def main():
    # Prompt for the user's name
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")
    
main()

while True:
    # Display the main menu
    print("1. Add Matrices")
    print("2. Check Rotation")
    print("3. Invert Dictionary")
    print("4. Convert Matrix to Dictionary")
    print("5. Check Palindrome")
    print("6. Search for an Element & Merge Sort")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_matrices()
    elif choice == "2":
        check_rotation()
    elif choice == "3":
        invert_dictionary()
    elif choice == "4":
        convert_matrix_to_dictionary()
    elif choice == "5":
        check_palindrome()
    elif choice == "6":
        search_element_and_merge_sort()
    elif choice == "7":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

