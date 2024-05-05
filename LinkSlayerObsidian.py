# Welcome to Link Slayer. Please read README.md for more information

import os
import sys
from typing import List

MAIN_EMOJI = "\U0001F525" * ("--no-emojis" not in sys.argv)


def bidirectional_pad(text: str, pad: str, num: int = 1) -> str:
    return (pad * num) + text + (pad * num)


def menu_select() -> str:
    return input(
        bidirectional_pad("What would you like to do?", MAIN_EMOJI, 3)
        + "\n"
        + bidirectional_pad("1. Read a file", MAIN_EMOJI)
        + "\n"
        + bidirectional_pad("2. Read a text from the stdin", MAIN_EMOJI)
        + "\n"
        + bidirectional_pad(
            "3. Read a file and append it to another file",
            MAIN_EMOJI,
        )
        + "\n"
        + bidirectional_pad("4. Exit", MAIN_EMOJI)
        + "\n"
    )


def intake_name(filename: str):
    """
    Function to intake a filename and open the file in read mode.
    If the file does not exist the function
    will be repeatedly ask for a valid filename.
    It return a list, with each element being a line from the file
    """
    while not os.path.isfile(filename):
        filename = input(
            bidirectional_pad(
                "File not found, please enter the name of the file",
                MAIN_EMOJI,
            )
        )

    with open(filename, "r", encoding="utf-8") as readfile:
        lines = readfile.readlines()
        return lines


def file_amalgam(lines):
    """
    Function to intake a filename and open the file in append mode.
    If the file does not exist the function
    will be repeatedly ask for a valid filename.
    """
    path = input(
        bidirectional_pad(
            "Please enter the name of the file you wish to add to",
            MAIN_EMOJI,
        )
        + "\n (This will overwrite any existing file of the same name) \n"
    )

    while not os.path.isfile(path):
        path = input(
            bidirectional_pad(
                "Please enter the name of the file you wish to add to",
                MAIN_EMOJI,
            )
            + "\n (This will overwrite any existing file of the same name) \n"
        )

    with open(
        path,
        "a",
        encoding="utf-8",
    ) as destination:
        new_data = slayer(lines)
        destination.writelines(new_data)

def colour_detect(line):
    colours = ["#FF5582A6", "#BD6500", "#BABD00", "#69E772", "#69E7E4", "#D2B3FFA6"]
    
    for colour in colours:
        if line.find(colour) != -1:
            print("\nColour checked:" + colour)
            return colour
        
    print(bidirectional_pad("Highlight colour not known", MAIN_EMOJI))
    return ''


# This should return the text, not write it to a file.
def slayer(lines) -> List[str]:
    """
    Intake a file object and a list of elements making of the contents of a previously read file.
    Removes all double equals signs that indicate highlighting
    Writes the contents of the list to the new file, unless a line contains a keyphrase that is meant to be excluded
    Returns the number of links removed
    """

    # Key is set to "imgur" as all images are linked to imgur
    key = "imgur"
    
    # Highlight key set to syntax used by Obisidian Highlightr Plugin
    highlight_key = '<mark style="background:'
    
    link_count = 0
    highlight_count = 0
    heading_count = 0
    
    #Flag to see if a highlight colour has been detected yet
    highlight_flag = False
    
    new_text = []
    
    
    for line in lines:
        line = str(line)
        
        while line.find("# ") != 1:  
            line.replace("### ", " ", 1)
            line = line.replace("# ", " ", 1)
            heading_count += 1

        #Detects if there is a highlight and what colour it is
        if highlight_key in line and highlight_flag == False:
            highlight_colour = colour_detect(line)
            highlight_flag = True
        
        # Replaces Highlightr syntaxs
        while line.find(highlight_key) != -1:
            line = line.replace(highlight_key, '', 1)
            line = line.replace(highlight_colour, '', 1)
            line = line.replace(';">', '', 1)
            line = line.replace('</mark>', '', 1)
            highlight_count += 1
        
        # Replaces markdown highlight syntax
        while line.find("==") != -1:
            line = line.replace("==", '', 1)
            highlight_count += 1
        
        # If the line is not an imgur link, it will be added to the new file 
        if key not in line:
            new_text.append(line)
        else:
            link_count += 1

    print(bidirectional_pad(f"{link_count} link(s) have been slain!", MAIN_EMOJI))
    print(bidirectional_pad(f"{highlight_count} highlight(s) have been slain!", MAIN_EMOJI))
    print(bidirectional_pad(f"{heading_count} heading(s) have been slain!", MAIN_EMOJI))
    return new_text


def write_new_file(data: str):
    filename = input(bidirectional_pad("Please enter the name of the new text file that will be summoned", MAIN_EMOJI,) + "\n")
    while os.path.isfile(filename):
        filename = input("\n" + bidirectional_pad("File already exists. Pick a different one.", MAIN_EMOJI) + "\n")
    with open(filename, "w", encoding="utf-8") as newfile:
        new_data = slayer(data)
        newfile.writelines(new_data)

def main():
    print(bidirectional_pad("WELCOME TO LINK SLAYER", MAIN_EMOJI))
    while (menu := menu_select()) != "4":
        match menu:
            case "1":
                # intakes name of file to be read
                filename = input(bidirectional_pad("Please enter the name of the text file you wish to cleanse of its sins", MAIN_EMOJI,) + "\n")
                # repetition in case 2
                lines = intake_name(filename)
                write_new_file(lines)

            case "2":
                # intakes text to be read
                # repetition in case 2
                lines = str(
                    input(
                        "\n\U0001F525 Please paste the text you wish to vanquish links from into the terminal (Right Click) \U0001F525\n"
                    )
                )
                write_new_file(lines)

            case "3":
                # appends new file to current file
                filename = input(
                    bidirectional_pad(
                        "Please enter the name of the text file you wish to cleanse of its sins and join in union with another cleansed file",
                        MAIN_EMOJI,
                    )
                )

                lines = intake_name(filename)

            case "4":
                print(bidirectional_pad("Fare thee well, Hero", MAIN_EMOJI))
                break

            case _:
                print(bidirectional_pad("Not a valid menu option", MAIN_EMOJI))


if __name__ == "__main__":
    main()
