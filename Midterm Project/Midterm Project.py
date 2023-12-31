#This statement is used to import the json module in Python,
# which provides methods for encoding and decoding JSON data
import json
#The requests module allows you to send HTTP requests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
#https://www.w3schools.com/python/module_requests.asp
import requests

#managing  tabs in a list called tabs
tabs = []

def fetch_html_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

#Function to open new tab
#https://www.honeybadger.io/blog/a-guide-to-exception-handling-in-python/ 
def open_tab ():
    while True:    
        try:
            title = input("Enter The Title of Wepsite : ")
            if not title:
                raise ValueError("Title cannot be empty.")
            
            url = input("Enter The URL example (www.google.com): ")
            if not url:
                raise ValueError("Url cannot be empty.")
            
#Check if the url start withe https:// 

            if not url.startswith("https://"):
                url = "https://" + url
     
            html_content = fetch_html_content(url)
            if html_content is not None:
                newTab = {"Title": title, "URL": url,"HTMLContent": html_content, "NestedTabs": []}
                tabs.append(newTab)
                print(f"Tab '{title}'opened successfully.")
                
                break
            else:
                print("Faild to open the tab Check the Url")
        except ValueError as ve:
            print(f"Error: {ve}")
        
    
 #Function to close tab by enter the index of tab .if not close last tab by press Enter   
def close_tab ():
    index = input("Enter the index of tab to close or Press Enter to close the last tab : ")
    if index == '':
        if tabs:
            closed_tab = tabs.pop()#The pop() method removes the element at the specified position.https://www.w3schools.com/python/ref_list_pop.asp
            print(f"Closed tab: '{closed_tab['Title']}'")
        else:
            print("No tabs to close.")
    else:
            index = int(index)
            if 0 <= index < len(tabs):
                closed_tab = tabs.pop(index)
                print(f"Closed tab: '{closed_tab['Title']}'")
            else:
                print("Invalid tab index.")
                
                
# Function to switch to a tab                
def switch_tab():
    if not tabs:
        print("No tabs available to switch.")
        return

    # Display existing tabs for reference
    print("Existing tabs:")
    display_all_tabs(tabs)

    index = input("Enter the index of the tab to switch to (Press Enter to switch to the last tab): ")

    if not index:
        if tabs:
            current_tab = tabs[-1]
            print(f"Switched to tab: '{current_tab['Title']}'")
            print(f"Displaying content of URL: {current_tab['URL']}")
        else:
            print("No tabs to switch to.")
    else:
        try:
            index = int(index)
        except ValueError:
            print("Invalid input. Please enter a valid index.")
            return

        if 0 <= index < len(tabs):
            current_tab = tabs[index]
            print(f"Switched to tab: '{current_tab['Title']}'")
            print(f"Displaying content of URL: {current_tab['URL']}")
            display_html_content(current_tab['URL'])
        else:
            print("Invalid tab index.")
                
            
#display html content by requests module               
def display_html_content(url):
    #Make an HTTP Get request to the url 
    response = requests.get(url)
    #Check if request was successful
    response.raise_for_status()
    print("HTML content: ")
    #Return the content of the response when make http request using request.get
    print(response.text)
           
 #Function to display parent tab and nested tab   
def display_all_tabs (tabs_list, depth=0):#depth parameter is used to keep track of the nesting level of the tabs. It is incremented by 1 each time the function is called recursively for nested tabs.
    
    if not tabs_list and depth == 0:
        print("No Tabs To Display")
        return
    for i, tab in enumerate(tabs_list):#enumerate function in Python is used to iterate over a sequence (such as a list, tuple, or string) https://www.geeksforgeeks.org/enumerate-in-python/
        print("  " * depth + f"{i + 1}. {tab['Title']}")
        display_all_tabs(tab['NestedTabs'], depth + 1)
    
#Function creat tabs in parent tab 
def open_nested_tab ():
    
    # Check if there are any tabs available
    if not tabs:
        print("No parent tabs available to open a nested tab.")
        return

    # Display existing tabs for reference
    print("Existing tabs:")
    display_all_tabs(tabs)

    # Get the index of the parent tab
    parent_index = input("Enter the index of the parent tab to open a nested tab: ")

    if not parent_index:
        print("Parent index cannot be empty.")
        return

    try:
        parent_index = int(parent_index)
    except ValueError:
        print("Invalid input. Please enter a valid index.")
        return

    # Check if the parent index is valid
    if 0 <= parent_index < len(tabs):
        parent_tab = tabs[parent_index]

        # Get information for the new nested tab
        title = input("Enter the Title of the nested tab: ")
        url = input("Enter the URL of the nested tab: ")

        # Add "https://" if it doesn't start with it
        if not url.startswith("https://"):
            url = "https://" + url

        try:
            # Fetch HTML content with error handling
            html_content = fetch_html_content(url)
        except requests.exceptions.RequestException as e:
            print(f"Failed to open the nested tab. Error: {e}")
            return

        new_nested_tab = {'Title': title, 'URL': url, 'HTMLContent': html_content, 'NestedTabs': []}
        parent_tab['NestedTabs'].append(new_nested_tab)
        print(f"Nested tab '{title}' opened successfully under parent tab '{parent_tab['Title']}'.")
    else:
        print("Invalid parent tab index.")
    
    
#Function to clear all tab
def clear_all_tabs():
    tabs.clear()
    print("All tabs cleared.")

#Function to save tabs in JSON file    
def save_tabs():
    
    file_path = input("Enter the file path to save the tabs: ")
    #Creat a list to store tab data
    tab_data = []
    for tab in tabs:
        tab_data.append({"Title": tab["Title"],"URL": tab["URL"],"HTMlContent": tab["HTMLContent"],"NestedTabs": tab["NestedTabs"]})

    try:
        with open(file_path, 'w') as file:#'w' write
            json.dump(tabs, file, indent=2)#Write — json.dump()
        print("Tabs saved to file successfully.")
    except FileNotFoundError:
        print(f"Error: The specified path '{file_path}' is not valid. Please provide a valid path.")
    except PermissionError:
        print(f"Error: Permission denied. Check if you have the necessary permissions to write to the specified file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 
#Function to import tabs from JSON file   
def import_tabs():
    global tabs
    
    file_path = input("Enter the file path to import tabs from: ")
    
    try:
        with open(file_path, 'r') as file:#'r' read
            tabs = json.load(file)#Write — json.dump()
        print("Tabs imported from file successfully.")
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'. Please check the file path and try again.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        return tabs



def exit():
    print("Exiting ")
    
def displayMenu():
    print("-----------------------------------")
    print("Welcome to FCS Browser Tabs Simulation")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tabs")
    print("6. Clear All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
    print("-----------------------------------")
    
def main():
    while True:
        displayMenu()
        choice = input("Enter your choice: ")
        if choice == '1':
            open_tab()
        elif choice == '2':
            close_tab()
        elif choice == '3':
            switch_tab()
        elif choice == '4':
            display_all_tabs(tabs)
        elif choice == '5':
            open_nested_tab()
        elif choice == '6':
            clear_all_tabs()
        elif choice == '7':
            save_tabs()
        elif choice == '8':
            import_tabs()
        elif choice == '9':
            exit()
            break
        else:
            print("invalid choice. Please choose a number from Menu. ")
            
#It Allows You to Execute Code When the File Runs as a Script,
# but Not When It’s Imported as a Module
#https://realpython.com/if-name-main-python/            
if __name__ == "__main__":
    main()
            
            
                      
            
                      