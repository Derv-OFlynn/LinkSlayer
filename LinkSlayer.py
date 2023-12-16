# Welcome to Link Slayer. Please read README.md for more information

def intake_name(filename : str):
    '''Function to intake a filename and open the file in read mode. If the file does not exist the function
    will be repeatedly ask for a valid filename. It return a list, with each element being a line from the file'''
    while True:
        try:
            readfile = open(filename, "r")
            lines = readfile.readlines()
            readfile.close()
            return lines
        except FileNotFoundError:
            filename = input("\nFile not found, please enter the name of a file within this directory \n")
            
def new_txt(new_name : str):
    '''Function to intake the new file name and open the file in write mode. Returns the file object'''
    while True:
        try:
            newfile = open(new_name, "w")
            return newfile
        except FileExistsError:
            new_name = input("\nInvalid File name. Try again.\n")
            
def slayer(newfile, lines):
    '''Function to intake a file object and a list of elements making of the contents of a previously read file.
    Writes the contents of the list to the new file, unless a line contains a keyphrase that is meant to be excluded
    Returns the number of links removed'''
    key = '%LOCAL_FILE%'

    link_count = 0

    for line in lines:
        if key not in str(line):
            newfile.write(str(line))
        else:
            link_count += 1
        
    newfile.close()
        
    return link_count
        

print("\n\U0001F525 WELCOME TO LINK SLAYER \U0001F525\n")

#intakes name of file to be read       
filename = input("\n\U0001F525 Please enter the name of the text file you wish to cleanse of its sins \U0001F525 \n")

lines = intake_name(filename)

#intakes name of file to be written to
new_name = input("\n\U0001F525 Please enter the name of the new text file that will be summoned \U0001F525 \n(This will overwrite any existing file of the same name) \n")

newfile = new_txt(new_name)

link_count = slayer(newfile, lines)
        
print("\n\U0001F525", link_count ,"link(s) have been slain! \U0001F525\n")