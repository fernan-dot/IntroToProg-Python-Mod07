# ------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrating how to simply store data in a binary file with error handling
# ChangeLog: (Who, When, What)
# Fernando Hernandez, 11/23/2019, Submit Assignment 07

# ------------------------------------------------- #

import pickle
strfirstName = str(input("Enter Your First Name --> "))
strlastName = str(input("Enter Your Last Name --> "))
intAge = ()

# Lets' error proof our input data

try:
    intAge = int(input("Enter Your Age in Numeric Format --> "))
except ValueError:
    print("The Information Entered Was Not Valid! ")
    input("Please, Hit Enter Key To Exit ")
lstuserData = [strfirstName, strlastName, intAge]

# Lets' store the data utilizing pickle.dump

objFile = open("AppData.dat" , "wb")
pickle.dump(lstuserData, objFile)
objFile.close()

# Let's read the data utilizing pickle.load

objFile = open("AppData.dat" , "rb")
objFileData = pickle.load(objFile)
objFile.close()
print("Here's the information entered..")
print(objFileData)
