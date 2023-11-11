import json

tabs = []

#Function to open new tab 
def openTab ():
    title = input("Enter The Title of Wepsite: ")
    url = input("Enter The URL: ")
    newTab = {"Title": title, "URL": url, "Nested": []}
    tabs.append(newTab)
    print(f"Tab '{title}'opened successfully.")
    
def closeTab ():
    pass
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
            
            
                      
            
                      