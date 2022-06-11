# In this assignment you will create a simple branching program.  the requirements are as follows:

# John wishes to go to a movie with his two friends, Sam, and Bob.
#  John is 15, Sam is 18, and Bob is 67.  The program will do the following:

# John will be told he cannot see the movie
# Sam will be charged $15 dollars
# Bob will be charged $5.

# Senior citizens (age 65+) will receive a $10 discount on the movie.

person1_age = int(input("Enter the age of John: "))
peron2_age = int(input("Enter the age of Sam: "))
perosn3_age = int(input("Enter the age of Bob: "))

print('-------people who will see the Movie-------')


# program to check John age
if person1_age < 18:
    print("John can not see the  movie")
elif person1_age >= 18 or person1_age < 65:
    print("John will charged 15$.")
else:
    print("John will charged 5$.")

# program to check Sam age
if peron2_age < 18:
    print("Sam can not see the  movie")
elif peron2_age >= 18 or peron2_age < 65:
    print("Sam will charged 15$.")
else:
    print("Sam will charged 5$.")

# program to check Bob age
if perosn3_age < 18:
    print("Bob can not see the  movie")
elif perosn3_age < 65:
    print("Bob will charged 15$.")
else:
    print("Bob will charged $5 after a $10 discount has been applied.")