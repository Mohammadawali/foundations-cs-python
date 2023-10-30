
def add_matrices():
    # Function to add matrices
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

def check_rotation():
    # Function to check rotation
    pass

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


def convert_matrix_to_dictionary():
    # Function to convert a matrix to a dictionary
    pass

def check_palindrome():
    # Function to check if a string is a palindrome
    pass

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