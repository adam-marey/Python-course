# In this assignment you will design a program to give customers the correct change. 

# Here are the parameters:

# Coins to use and their values:  Half Dollars (50) Quarter Dollars (25) Dimes (10) Nickels (5) Pennies (1)

# The user will enter a number between 1 and 99.  If the number is outside of that range, you will inform the user and terminate the program.

# You will use as few coins as possible.  For example, if the user enters "50", you will give the answer as "One Half Dollar" and not "5 Dimes" or "50 Pennies".
# You will loop through each coin denomination, with the possible exception of the penny. 
# Here is a hint:
# If the number is 99, then subtract 50 from the number using a loop.  This leaves 49, with one half dollar used. 
# Next, subtract 25 from the total using a loop.  This leaves 24, with one quarter used
# Next, subtract 10 cents from the total in a loop.  This will leave 4 cents, with two dimes used.
# Finally record the four pennies left over.
# The output should read something like:  "You have one half dollar, one quarter, two dimes, and four pennies".
# Function to compute the correct change based
# on the number of coins passed as parameter
def customer_changes(coins):
    
    # Creating an array of strings which stores the
    # decimal digits in form of alphabetical words
    digits_in_word = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
    
    # Counting the number of half dollars
    number_of_half_dollar = 0
    while(coins >= 50):
        coins = coins - 50
        number_of_half_dollar = number_of_half_dollar + 1
    
    # Counting the number of quarter dollars
    number_of_quarter_dollar = 0
    while(coins >= 25):
        coins = coins - 25
        number_of_quarter_dollar = number_of_quarter_dollar + 1
    
    # Counting the number of dimes
    number_of_dimes = 0
    while(coins >= 10):
        coins = coins - 10
        number_of_dimes = number_of_dimes + 1
    
    # Counting the number of nickels
    number_of_nickels = 0
    while(coins >= 5):
        coins = coins - 5
        number_of_nickels = number_of_nickels + 1
    
    # Counting the number of pennies
    number_of_pennies = 0
    while(coins >= 1):
        coins = coins - 1
        number_of_pennies = number_of_pennies + 1
    
    # Now formatting the output string based on the number of each type of coins
    output = "You have "
    
    if(number_of_half_dollar > 0):
        output = output + digits_in_word[number_of_half_dollar] + " half dollar "
        
    if(number_of_quarter_dollar > 0):
        output = output + digits_in_word[number_of_quarter_dollar]  + " quarter dollar "
        
    if(number_of_dimes > 0):
        output = output + digits_in_word[number_of_dimes] + " dime "
        
    if(number_of_nickels > 0):
        output = output + digits_in_word[number_of_nickels] + " nickel "
        
    if(number_of_pennies > 0):
        output = output + digits_in_word[number_of_pennies] + " pennies"
    
    # Finally printing the formatted output string
    print(output)

# Taking input the number of coins from the user
coins = int(input("Enter a number between 1 and 99: "))

# Checking the input belongs to the valid range or not
if(1 <= coins <= 99):
    # Calling a function to print the correct change
    customer_changes(coins)
else:
    print("You have entered a number that is outside of that range")
