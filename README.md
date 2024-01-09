# LINK SLAYER

The purpose of this is to be able to copy notes from Remnote (a note-taking app) and paste them into a TTS (Text to Speech) Reader without the URLs. 
Images show up as links in plaintext and are not useful when using a TTS reader as a study/accessibility aid.

Link slayer is a python script that reads a file from its directory and writes the contents to a new file of your choosing, excluding URLs from the old file.

## User Process
  
1. The user is asked to enter the name of the file they wish to read from. If it exists in the directory, it will be opened in Read mode.
2. The user is asked to enter the name of the new file that will be created without the URLs.
3. A new file is created in the same directory and the program informs the user how many links were removed

## Link Detection
Currently, the only links that LinkSlayer will remove are local URLs. This is because it will not write lines to the new file if they contain the string '%LOCAL_FILE%' or 'remnote-user', as this is how links are formatted in RemNote.

## Screenshot of the Program (Used throught terminal input)

![LinkSlayerEX1](https://github.com/Derv-OFlynn/LinkSlayer/blob/main/Images/LinkSlayerEX1.png)

