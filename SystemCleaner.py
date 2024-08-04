import os

'''


#Make a project in python
#A script that can clear cache files as well as temp files
- should be able to list files with a directory
- File Detection

#Side Objectives - Repair system drivers when ran

'''
#1.)research what os does in python 
#os module in Python provides a way to interact with the operating system



'''
Logic:

On startup ask user to input path diectory, if it exists use os module to get access to it then ask the user what they want to do within it
If path does not exist syserror -> "The path entered could not be found/may not exist"

/Clr temp logic
If the user asks to clr temp files then ________ -> find a way to list them

/ls directory logic
If user wants to know the current directory os.getcwd

/ls files in directory logic
If user wants to list files in directory --->
'''

user_path = input("Input Path Directory: ")
#need a while loop that continues the question as long as the directory is wrong

choices = ["Clr temp files", "List Current Directory"]
print(choices)



# os.listdir() - used to get the list of all files and directories in the specified directory.
# 
dir_files= os.listdir(user_path)
print(dir_files)


user_command = input("Enter: ")
# while (user_command not in choices):
#     user_command = input("Enter: ")


#     if (user_command == choices[0]):
#         #code for clr temp files
#     elif (user_command == choices[1]):

#         #code for list current dir









    















#2.) Determine the paths of the cache and temp folders you want to clear, maybe you can have user input for this, then some try and exceptions if the path is incorrect
#We only want to clear specific file types 









#3.)If you want to clear specific file types, use string operations or regular expressions to check the file type.


#4.)With error handling -  Print informative messages to indicate the progress and results of the script.


#5.)Test your script on a small scale or with backup data to ensure it works as expected.


'''
#Print statements for exceptions 
- Incorrect command.
-File does not exist
-Temp File clear attempt Failed.
-
 
'''

