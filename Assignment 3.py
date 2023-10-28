def main():
    # Prompt for the user's name
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")

# Call the main function
main()

def add_matrices():
    # Function to add matrices
    pass

def check_rotation():
    # Function to check rotation
    pass

def invert_dictionary():
    # Function to invert a dictionary
    pass

def convert_matrix_to_dictionary():
    # Function to convert a matrix to a dictionary
    pass

def check_palindrome():
    # Function to check if a string is a palindrome
    pass

def search_element_and_merge_sort():
    # Function to search for an element and perform merge sort
    pass

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

