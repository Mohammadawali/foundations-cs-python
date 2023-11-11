import json

tabs = []

#Function to open new tab 
def openTab ():
    title = input("Enter The Title of Wepsite: ")
    url = input("Enter The URL: ")
    newTab = {"Title": title, "URL": url, "Nested": []}
    tabs.append(newTab)
    print(f"Tab '{title}'opened successfully.")
 #Function to close tab    
def closeTab ():
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
                
def switchTab ():
    pass
def displayAllTabs ():
    pass
def openNastedTab ():
    pass
def clearAllTabs():
    pass
def saveTabs():
    pass
def importTabs():
    pass
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
        choice = input("Enter your choice")
        if choice == '1':
            openTab()
        elif choice == '2':
            closeTab()
        elif choice == '3':
            switchTab()
        elif choice == '4':
            displayAllTabs()
        elif choice == '5':
            openNastedTab()
        elif choice == '6':
            clearAllTabs()
        elif choice == '7':
            saveTabs()
        elif choice == '8':
            importTabs()
        elif choice == '9':
            exit()
            break
        else:
            print("invalid choice. Please choose a number from Menu. ")
            
if __name__ == "__main__":
    main()
            
            
                      
            
                      