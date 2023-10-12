def create_files():
    directory = input('''What\'s the directory of the file you're trying to create for your journal?
NOTE: File will be a dsu file\n''').strip()
    name = input('What do you want to name your file?\n').strip()
    final = [directory,'-n',name]
    return final

def open_files():
    directory = input('''What\'s the directory of the file of journal you're trying to access? 
    NOTE: File has to be a .dsu file
    ex. c:\\users\\andyh\\desktop\\myjournal.dsu\n''').strip()
    final = [directory]
    return final

def edit_files():
    truths = True
    final = ''
    x = ''' Here's the Edit Menu:
    -usr [USERNAME]

    -pwd [PASSWORD]

    -bio [BIO]

    -addpost [NEW POST]

    -delpost [ID] (a number such as 1, 2, 3...)
    
    ** NO WHITESPACES IN USERNAME OR PASSWORD, IF YOU DO WILL RESULT IN ERROR **
    ** MAKE SURE EVERYYTHING EXCEPT FOR THE ID NUMBER IS IN QUOTES "" '''
    print(x)

    while truths:
        selection = input('''Enter a edit:
        Just the first part:
            ex. -usr, -pwd, -bio...\n''')
        change = input('''Enter the change you want to make\n''')
        end = input('''Do you want to make more edits? y/n:
        ** Only enter the letter y or n\n''').strip()
        one = final
        two = selection + ' ' + change + ' '
        final = one + two
        if end == 'n':
            truths = False
    
    updated_final = final.strip()

    return updated_final

def print_files():
    truths = True
    final = ''
    x = '''Here's the Print Menu:
    -usr Prints the username stored in the profile object

    -pwd Prints the password stored in the profile object

    -bio Prints the bio stored in the profile object

    -posts Prints all posts stored in the profile object with id (using list index is fine)

    -post [ID] Prints post identified by ID numbered starting from 1

    -all Prints all content stored in the profile object'''
    print(x)
    while truths:
        selection = input('''Enter what you want to print out:
        Just the first part:
            ex. -usr, -pwd, -bio...\n''')
        end = input('''Do you want to print anything else? y/n:
        ** Only enter the letter y or n\n''').strip()
        one = final
        two = selection + ' '
        final = one + two
        if end == 'n':
            truths = False
    
    updated_final = final.strip()

    return updated_final

def get_info():
    condition = False
    server = input("What server are you trying to connect to? ")
    port = input("What port are you trying to connec to?")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    message = input("What message would you like to send? ")
    x = input("Would you like to add a bio? y/n")
    if x == "y":
        bio = input("Enter a bio: ")
        condition = True
    elif x == "n":
        pass
    else:
        pass
    if condition == False:
        master_inputs = [server, username, password, message, port]
        return master_inputs
    else:
        master_inputs = [server, username, password, message, bio, port]
        return master_inputs

def get_info1():
    condition = False

    message = input("What message would you like to send? ")
    x = input("Would you like to add a bio? y/n")
    if x == "y":
        bio = input("Enter a bio: ")
        condition = True
    elif x == "n":
        pass
    else:
        pass
    if condition == False:
        master_inputs = [message]
        return master_inputs
    else:
        master_inputs = [message, bio]
        return master_inputs

def postJournal():
    directory = input('''What\'s the directory of the file of journal you're trying to post to the DSP server? 
    NOTE: File has to be a .dsu file
    ex. c:\\users\\andyh\\desktop\\myjournal.dsu\n''').strip()
    journalNumber = input('Which Journal Entry # would you like to post?')
    final = [directory, journalNumber]
    return final 

def start():
    x = input('''Would you like to go create a file or go online?
    - Enter C to create a file
    - Enter E to edit a file
    - Enter P to print contents within a file
    - Enter O to open a file
    - Enter A to go online
    - Enter U to post a journal
    - Enter Q to quit\n''').upper().strip()
    list1 = ['C', 'E', 'P','O', 'A', 'Q', 'U']
    if x in list1:
        if x == list1[0]: ## for Create
            return "C"
        elif x == list1[1]: ## Edit
            return "E"
        elif x == list1[2]: ## Print
            return "P"
        elif x == list1[3]: ## Open
            return "O"
        elif x == list1[4]: ## Go online(A)
            return True
        elif x == list1[6]: ## Upload a journal
            return "U"
        elif x == list1[5]: ## Quit
            print("Goodbye!")
            return 'Q'
    else:
        print('Invalid Input, Please try again!')
        start()

if __name__ == "__main__":
    start()