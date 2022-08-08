
# only accept whole numbers
def getValidWholeNumber():
    while True:
        try:
            num = input('Enter a whole number: ')
            num = int(num)
            return num
        except:
            print('Error: Please enter a whole number.')

# how many numbers are in a string.
# function accepts a sentence string returns the number of digits in it
def numbersInString(sentence):
    countDigits=0
    for letter in sentence:
        if letter.isdigit():
            countDigits+=1
    return countDigits

#not allow spaces.
def getInputWithoutSpace():
    while True:
        word = input('Enter a word without any spaces: ')
        if ' ' in word:
            print('Error: Entered word contains spaces')
        else:
            return word

def main():
    getValidNumber()
    getValidLetters()
    print(numbersInString('1tqe26rw2'))
    getValidWholeNumber()
    getInputWithoutSpace()
main()