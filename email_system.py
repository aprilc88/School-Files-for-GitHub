'''
The purpose of this program is demonstrate use of dictionaries by allowing a user
to search, add, edit and delete a person and their email.

Author: April Carchedi
'''
import pickle

# Constants for Menu
FIND = 1
ADD = 2
EDIT = 3
DELETE = 4
QUIT = 5

def main():
    # Empty Dictionary.
    EmailList = {'Tasha Yar': 'yarT@starfleet.net',
                 'JeanLuc Picard': 'picardJ@starfleet.net',
                 'Beverly Crusher': 'crusherB@starfleet.net'}
    selection = 0

    while selection != QUIT:
        # Get menu selection.
        selection = get_choice()

        # Menu
        if selection == FIND:
            find(EmailList)
        elif selection == ADD:
            add(EmailList)
        elif selection == EDIT:
            edit(EmailList)
        elif selection == DELETE:
            delete(EmailList)
    # output_file.close()

def get_choice():

    print("Names and Emails System")
    print("-----------------------\n")
    print("Select from the following menu:")
    print("1. E-Mail Lookup.")
    print("2. Add New Name & Email.")
    print("3. Change Exisiting E-Mail.")
    print("4. Delete Exisitng Name & E-Mail.")
    print("5. Quit Program.")
    print("-----------------------\n")
    selection = int(input("Enter # of your selection: "))

    while selection < FIND > QUIT:
        selection = int(input("Enter valid selection: "))

    return selection

# Find function.
def find(EmailList):
    name = input("Enter name to search: ")
    print(EmailList.get(name, 'Not Found\n'))
    
# Add function.
def add(EmailList):
    output_file = open('EmailList.txt', 'wb')
    name = input("Enter the name: ")
    email = input("Enter their email: ")

    # Check if there already is an entry.
    if name not in EmailList:
        EmailList[name] = email
        pickle.dump(EmailList, output_file)
        print(name, " has been added.\n\n")
    else:
        print("That person already exists.\n\n")
    output_file.close()
        
# Change/Update email function.
def edit(EmailList):
    output_file = open('EmailList.txt', 'wb')
    name = input("Enter name to edit email: ")
    if name in EmailList:
        email = input("Enter new email: ")
        EmailList[name] = email
        print(name, " email updated.")
        print(name, email, "\n\n")
    else:
        print("Name not found\n\n")
    output_file.close()

# Delete Function.
def delete(EmailList):
    output_file = open('EmailList.txt', 'wb')
    name = input("Enter name to be deleted: ")

    if name in EmailList:
        del EmailList[name]
    else:
        print("Name not found\n")
    output_file.close()
    
    

main()

'''
Sample 1:
Names and Emails System
-----------------------

Select from the following menu:
1. E-Mail Lookup.
2. Add New Name & Email.
3. Change Exisiting E-Mail.
4. Delete Exisitng Name & E-Mail.
5. Quit Program.
-----------------------

Enter # of your selection: 2
Enter the name: Wesley Crusher
Enter their email: crusherW@starfleet.net
Names and Emails System
-----------------------

Select from the following menu:
1. E-Mail Lookup.
2. Add New Name & Email.
3. Change Exisiting E-Mail.
4. Delete Exisitng Name & E-Mail.
5. Quit Program.
-----------------------

Enter # of your selection: 1
Enter name to search: Wesley Crusher
crusherW@starfleet.net



Sample 2:
Names and Emails System
-----------------------

Select from the following menu:
1. E-Mail Lookup.
2. Add New Name & Email.
3. Change Exisiting E-Mail.
4. Delete Exisitng Name & E-Mail.
5. Quit Program.
-----------------------

Enter # of your selection: 3
Enter name to edit email: Tasha Yar
Enter new email: newEMAIL@email.org
Tasha Yar  email updated.
Tasha Yar newEMAIL@email.org 



Sample 3:
Names and Emails System
-----------------------

Select from the following menu:
1. E-Mail Lookup.
2. Add New Name & Email.
3. Change Exisiting E-Mail.
4. Delete Exisitng Name & E-Mail.
5. Quit Program.
-----------------------

Enter # of your selection: 2
Enter the name: TEst
Enter their email: test
TEst  has been added.
'''
