import os
from pyfiglet import Figlet
from colorama import Fore

#clear terminal
os.system("clear")



#create banner
banner = Figlet()
#banner print
print(Fore.RED + banner.renderText('M R . 1 3') )
print(Fore.RED + ">add text in .txt ------------v.1<")
print(Fore.WHITE) 

#Question to identify the existence of the file
question = input("Do you have a file or do you want me to create one for you? (i have/u)")


if question == "i have":
    #To get the file name
    file_name = input("Enter your file name in this directory ==> ")
    
    if '.txt' in file_name:
        #open text file & 'a+' is a mode and here it does Opens a file for appending
        file = open(file_name, "a+")
        #text from add in txt file
        textInput = input("Enter your text from add to " + file_name + ' ==> ' )
        #write text in file.txt
        file.write(textInput)
        #close file.txt
        file.close()
    #from create new file.txt
    else:
        #open text file & 'a+' is a mode and here it does Opens a file for appending
        #If the file format was not entered
        file = open(file_name + ".txt", "a+")
        #text from add in txt file
        textInput = input("Enter your text from add to " + file_name + '.txt' + ' ==> ' )
        #write text in file.txt
        file.write(textInput)
        #close file.txt
        file.close()
elif question == "u" :
    create_file = input('Enter your file name ==> ')
    if '.txt' in create_file:
        #open text file & 'a+' is a mode and here it does Opens a file for appending
        file = open(create_file, "a+")
        #text from add in txt file
        textInput = input("Enter your text from add to " + create_file + ' ==> ' )
        #write text in file.txt
        file.write(textInput)
        #close file.txt
        file.close()
    #from create new file.txt
    else:
        #open text file & 'a+' is a mode and here it does Opens a file for appending
        #If the file format was not entered
        file = open(create_file+ ".txt", "a+")
        #text from add in txt file
        textInput = input("Enter your text from add to " + create_file + '.txt' + ' ==> ' )
        #write text in file.txt
        file.write(textInput)
        #close file.txt
        file.close()
