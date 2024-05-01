# LINK SLAYER

The purpose of this is to be able to copy notes from Remnote and Obsidian (note-taking applications) and paste them into a TTS (Text to Speech) Reader without the URLs. 
Images show up as links in plaintext and are not useful when using a TTS reader as a study/accessibility aid.

LinkSlayer is a python script that reads a file from its directory and writes the contents to a new file of your choosing, excluding URLs from the old file.

## User Process
  
1. The user is asked to enter the name of the file they wish to read from. If it exists in the directory, it will be opened in Read mode.
2. The user is asked to enter the name of the new file that will be created without the URLs.
3. A new file is created in the same directory and the program informs the user how many links were removed

## Link Detection

Linkslayer will "detect" links by searching for keywords in the given document. Image links take up their own lines so when a line is detected as having a link, the line will not be appended to the new file.

#### Remnote
LinkSlayer will only remove local URLs. The keys are set to '%LOCAL_FILE%' or 'remnote-user', as this is how links are formatted in Remnote. Found in LinkslayerRemnote.py

#### Obsidian
Linkslayer will remove both markdown highlights ("==") and highlights that are formatted by the Highlightr Plugin (e.g. ``<mark style="background: #BD6500;">Lorem Ipsum:</mark>``). Found in LinkslayerObsidian.py

## Screenshot of the Program (Used throught terminal input)

![LinkSlayerObsidianExample](https://i.imgur.com/xeY5nXj.png)