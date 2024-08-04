import os

#imported to monitor files
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

#shift + command +G in finder to get path of a file

#Examples

#File - /Users/stefan/Desktop/Self-Projects/filedetector.py
#Folder - /Users/stefan/Desktop/Self-Projects
#Download folder path -/Users/stefan/Library/Mobile Documents/com~apple~CloudDocs/Downloads


#let user create file
in_progress = True
while in_progress== True:
    user_command = input("1.)Create a file \n2.)Check existing path: \n3.)Sort Files \nWhat would you like to do?: ")

    if (user_command =='1'):
        name_file = input("Where would you like the file to be located?: ")
        #
    
    elif (user_command=='3'):
        source_dir = input("Enter Directory Path to sort: ")
        with os.scandir(source_dir) as entries:
            for piece in entries:
                print(piece.name)
    elif (user_command =='Exit'):
        print("Goodbye!")
        in_progress= False
        break

    # #checking path existence + number of lines within it
    # elif (user_command =='2'):
    #     file_path = input("Give Path: ")
    #     if os.path.exists(file_path):
    #         print("The given path location exists.")


    #     elif os.path.isfile(file_path):
    #         print("file has been found.")
    #         try:
    #             line_counter=0
    #             with open(file_path, 'r') as file:
    #                 for line in file:
    #                     line_counter +=1
    #             print("# of lines: "+ str(line_counter))
    #             #IOError - an error when opening a file 
    #         except IOError:
    #             print("Issue with reading # of lines in file")



    #         gonga = input("See contents of file? ")
    #         if (gonga =='yes'):
    #             #logic for number line count




    #     #     elif (gonga =='2'):
    #     #         #logic for showing files contents 

    #     # elif os.path.isdir(file_path):
    #     #     print("The path given is a directory within your system.")
    #     #     listdir = input("Would you like to list all known files within this directory?: ")
    #     #     if(listdir == 'yes'):
    #     #         #list everything within specific directory
    #     #         print("All known files within given directory:\n " +os.listdir(file_path))
            
    #     #     #Check elif statements and fix os.path.isfile
    #     # else:
    #     #     print("Within the gc apes exist")
