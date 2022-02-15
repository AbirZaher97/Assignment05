# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# AbirZaher,02.14.22
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# try to load data from ToDoList.txt into a list of dictionary rows
try:
    # open file to read
    objFile = open('ToDoList.txt', 'r')
    for row in objFile:
        strData = row.split(",")
        # to convert row to dicRow
        dicRow = {'Task': strData[0], 'Priority': strData[1].strip()}
        # append dictionary to table list
        lstTable.append(dicRow)
    objFile.close()
# to create a txt file if the ToDoList.txt file doesn't exist
except:
    objFile = open("ToDoList.txt", 'w')
    objFile.close()
    print("ToDoList.txt not found")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
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
    if strChoice.strip() == '1':
        print(' Your current data is: ')
        for row in lstTable:
            print("Task: ", row['Task'], '|', "Priority: ", row['Priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        print("Add an item to your to do list")
        # ask user to enter input
        strTask = str(input("Enter a Task: "))
        strPriority = str(input("Enter the Priority of the task: "))
        # create dicRow
        dicRow = {'Task': strTask, 'Priority': strPriority}
        # append dicRow to table list
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strRem = input("Which task would you like to remove? ")
        for row in lstTable:
            # find if items match
            if row['Task'].lower() == strRem.lower():
                # if item match remove item
                lstTable.remove(row)
                print("Task: " + strRem + "\nthe task is removed from the list")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        # open file to write
        objFile = open('ToDoList.txt', 'w')
        # to go through each row in lstTable
        for row in lstTable:
            objFile.write((row['Task']) + "," + (row['Priority']) + "\n")
            print("\nData was saved")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print('Would you like to save your data?')
        strOption = str(input('Enter y or n : '))

        # if user chose y the data will be written in txt file
        if strOption.lower() == 'y':
            break  # and Exit the program
    else:
        continue
