# Welcome to Link Slayer. Please read README.md for more information
def menu_select():
    while True:
        try:
            menu = int(input("\n\U0001F525 What would you like to do? \U0001F525\n \
                \n\U0001F5251. Read a file in this directory \U0001F525 \
                \n\U0001F5252. Read a file from the terminal \U0001F525 \
                \n\U0001F5253. Read a file from this directory and append it to another file in this directory \U0001F525 \
                \n\U0001F5254. Exit  \U0001F525\n"))
            return menu
        except TypeError:
            print("\nError: Invalid character entered. Please enter a single digit integer\n")
            menu = int(input("\n\U0001F525 What would you like to do? \U0001F525\n"))
            
            
def intake_name(filename : str):
    '''Function to intake a filename and open the file in read mode. If the file does not exist the function
    will be repeatedly ask for a valid filename. It return a list, with each element being a line from the file'''
    while True:
        try:
            readfile = open(filename, "r", encoding='utf-8')
            lines = readfile.readlines()
            readfile.close()
            return lines
        except FileNotFoundError:
            filename = input("\nFile not found, please enter the name of a file within this directory \n")
            
def new_txt(new_name : str):
    '''Function to intake the new file name and open the file in write mode. Returns the file object'''
    while True:
        try:
            newfile = open(new_name, "w", encoding='utf-8')
            return newfile
        except FileExistsError:
            new_name = input("\nInvalid File name. Try again.\n")
            
def file_amalgam(lines):
    '''Function to intake a filename and open the file in append mode. If the file does not exist the function
    will be repeatedly ask for a valid filename.'''
    
    while True:
        try:
            
            destination = open(input("\n\U0001F525 Please enter the name of the new text file you wish to add this file to \U0001F525 \n(This will overwrite any existing file of the same name) \n"), "a")
            slayer(destination, lines)
            
            return
        except FileNotFoundError:
            
            destination = open(input("\n\U0001F525 File Not Found. Please enter the name of the new text file you wish to add this file to \U0001F525 \n(This will overwrite any existing file of the same name) \n"), "a")
    
            
def slayer(newfile, lines):
    '''Function to intake a file object and a list of elements making of the contents of a previously read file.
    Writes the contents of the list to the new file, unless a line contains a keyphrase that is meant to be excluded
    Returns the number of links removed'''
    
    key = '%LOCAL_FILE%'
    key2 = 'remnote-user'

    link_count = 0

    for line in lines:
        if key not in str(line):
            if key2 not in str(line):
                newfile.write(str(line))
            else:
                link_count += 1
        else:
            link_count += 1
        
    newfile.close()
        
    return link_count
        

print("\n\U0001F525 WELCOME TO LINK SLAYER \U0001F525\n")

menu = 0

while menu != 4:
    
    menu = menu_select()
    
    match menu:
        
        case 1:
            #intakes name of file to be read       
            filename = input("\n\U0001F525 Please enter the name of the text file you wish to cleanse of its sins \U0001F525 \n")

            lines = intake_name(filename)

            #intakes name of file to be written to
            new_name = input("\n\U0001F525 Please enter the name of the new text file that will be summoned \U0001F525 \n(This will overwrite any existing file of the same name) \n")

            newfile = new_txt(new_name)

            link_count = slayer(newfile, lines)
                    
            print("\n\U0001F525", link_count ,"link(s) have been slain! \U0001F525\n")
                
        case 2:
            #intakes text to be read       

            lines = str(input("\n\U0001F525 Please paste the text you wish to vanquish links from into the terminal (Right Click) \U0001F525\n"))

            #intakes name of file to be written to
            new_name = input("\n\U0001F525 Please enter the name of the new text file that will be summoned \U0001F525 \n(This will overwrite any existing file of the same name) \n")

            newfile = new_txt(new_name)

            link_count = slayer(newfile, lines)
                    
            print("\n\U0001F525", link_count ,"link(s) have been slain! \U0001F525\n")
            
        case 3:
            #appends new file to current file
            filename = input("\n\U0001F525 Please enter the name of the text file you wish to cleanse of its sins and join in union with another cleansed file\U0001F525 \n")

            lines = intake_name(filename)
            
            
        case 4:
            print("\n\U0001F525 Fare thee well, Hero \U0001F525\n")
            break    
        
        case _:
            print("\n\U0001F525 Not a valid menu option \U0001F525\n")
            