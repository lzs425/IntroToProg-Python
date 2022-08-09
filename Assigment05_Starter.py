# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Linda Shmait,08/08/22, Added code to complete assignment 5
# Linda Shmait,08/09/22, Adjusted Option 3 code to remove duplicates
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strItem = ""
strValue = ""
# objFile = open("ToDoList.txt", "a") to create file
# objFile.close() to close file

# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Item": lstRow[0], "Value": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
       # TODO: Add Code Here
        for row in lstTable:
            print(row["Item"] + "," + row["Value"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strItem = input("Item: ")
        strValue = input("Value: ")
        dicRow = {"Item": strItem, "Value": strValue}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strItem = input("Item to Remove: ")
        Found = False
        for row in lstTable:
            if row["Item"].lower() == strItem.lower():
                lstTable.remove(row)
                Found = True
                print(strItem + " has been removed from the list.")
                continue #what if an entry is in more than once?
        if Found == False:
            print(strItem + " not found.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for dicRow in lstTable:
            objFile.write(str(dicRow["Item"]) + "," + str(dicRow["Value"]) + "\n")
        objFile.close()
        print("Your data was saved to ToDoList.txt.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("Are you sure you would like to exit the program?")
        strSaveOption = input("Enter 'y' or 'n': ")
        if strSaveOption.lower() == 'y':
            print("The program has closed.")
            break  # and Exit the program
        elif strSaveOption.lower() == 'n':
            print("You will be routed to the main menu.")
            continue
        else:
            print("Only enter 'y' or 'n'. You will be taken to the main menu now.")
            continue

