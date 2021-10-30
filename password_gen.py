# python3
# Password Generation Utility
# CYB333 Final Project
# Yamyllett Jimenez-Rodriguez

# Generates a user-inputted number of passwords of user-inputted length

# Imports; using string for easy access to lists of ASCII characters and random for the randomization
import random
import string

# Defining some global variables

inputSamples = 0
inputLength = 0
cont = False
genPass = []


# Function definitions
def getSamplesNum():
    try:
        global inputSamples
        inputSamples = int(input('Generate how many passwords? '))
        return True
    except ValueError:
        print('Invalid input, please try again.')
        return False


# Same idea as getSamplesNum but for length
def getSamplesLength():
    try:
        global inputLength
        inputLength = int(input('Desired password length (min 12 recommended): '))
        return True
    except ValueError:
        print('Invalid input, please try again')
        return False


# Returns a randomly generated password of the desired length
def passGen():
    pword = ''
    for j in range(inputLength):
        pword += random.choice(asciiAll)
    return pword


# Main menu: prompt user to select choice
print('Hello, Welcome to Random Password Generator!')

# Get number of samples to generate using earlier functions
while cont is False:
    cont = getSamplesNum()
# Get length of samples to generate
cont = False
while cont is False:
    cont = getSamplesLength()


print('\nGenerating', inputSamples, 'passwords with', inputLength, 'characters...')
# Establish a base character set to pull from
asciiLow = string.ascii_lowercase
asciiUp = string.ascii_uppercase
asciiNum = string.digits
asciiSym = string.punctuation
asciiAll = asciiLow + asciiUp + asciiNum + asciiSym
leet_dict = dict(zip("aeilot", "431|07"))


def leet(txt):
    return txt.lower().translate(str.maketrans(leet_dict))

# Loop to iterate through the length of the password
# Adds each newly generated password to the list defined at the beginning


for i in range(inputSamples):
    pword = passGen()
    # for j in range(inputLength):
    #    pword += random.choice(asciiAll)
    if pword in genPass:
        print('Generated a duplicate, regenerating!')
        pword = passGen()

    genPass.insert(i, pword)

# Printing newly generated passwords
print('\nGenerated', inputSamples, 'passwords:\n')
for i in genPass:
    print(i)
print('\n')

# Using the top 10000 most common passwords from the OWASP SecList Project in a text file
# Using the passwords.txt file to read the list into a list
# Create list of common passwords from file
bank = open('passwords.txt', 'r')
parse = []

for i in bank:
    words = i.split()
    for a in words:
        parse.append(a)

# Check generated passwords against list
print('Checking generated passwords against list of common passwords...')
present = False
for i in genPass:
    if i in parse:
        print('is on the list of commonly used passwords, recommend not using and regenerating as needed.')
        present = True
if present is False:
    print('No matches found!')
