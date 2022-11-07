# David Garrett
# EET-107-100 Chapter 6 Lab 1
# 3-10-2021

def inputInfo():  # Asks user to input their name, street address, city, state, and zip code
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    currentStreetAddress = input('Enter your street address: ')
    currentCity = input('Enter your city: ')
    currentState = input('Enter your state: ')
    currentZipCode = input('Enter your zip code: ')
    fullName = firstName + ' ' + lastName
    cityStateZipCode = currentCity + ', ' + currentState + ' ' + currentZipCode
    allInfo = [fullName, currentStreetAddress, cityStateZipCode]
    return allInfo

def writeToFile(a):  # Passes user info to function and writes it to file
    out_file = open(nameOfFile + '.txt', mode='w')
    for i in a:
        out_file.write(i)
        out_file.write('\n')
    print()

def readTheFile(nameOfTheFile2):  # User inputs the name of file and function prints out the content
    while True:
        try:  # Try/except to deal with a situation where file cannot be found
            infile = open(nameOfTheFile2 + '.txt', 'r')
            break
        except FileNotFoundError:
            print('File doesn\'t exist.\n')  # User must put in existing file
            nameOfTheFile2 = input('What is the name of a file you want to read? ')
            continue
    fileContents = infile.read()
    print(fileContents)

nameOfFile = input('What is the name of a file you want to work with? ')  # Asks user for name of the file

while True:  # Asks user if he or she wants to read file, write to file, or exit
    readFromOrWriteTo = input('Press "r" to read to the file, "w" to write to file, or "e" to exit. ')
    if readFromOrWriteTo == 'r':
        readTheFile(nameOfFile)
    elif readFromOrWriteTo == 'w':
        userInfo = inputInfo()
        writeToFile(userInfo)
    elif readFromOrWriteTo == 'e':
        exit()
    else:
        print('Invalid Input.\n')