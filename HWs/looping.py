
def my_changes(coins):
    nums_strings = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
  
    # total of half dollars
    output = "You have "
    half_dollar = 0
    while(coins >= 50):
        coins -= 50
        half_dollar += 1
    if(half_dollar > 0):
      output = output + nums_strings[half_dollar] + " half dollar, "
    
    # total of quarter dollars
    quarter_dollar = 0
    while(coins >= 25):
        coins -= 25
        quarter_dollar += 1
    if(quarter_dollar > 0):
      output = output + nums_strings[quarter_dollar]  + " quarter dollar, "
    
    # total of dimes
    num_dimes = 0
    while(coins >= 10):
        coins -= 10
        num_dimes += 1
    if(num_dimes > 0):
      output = output + nums_strings[num_dimes] + " dime, "
    
    # total of pennies
    nums_pennies = 0
    while(coins >= 1):
        coins -= 1
        nums_pennies += 1
    if(nums_pennies > 0):
      output = output + nums_strings[nums_pennies] + " pennies"

    print(output)

coins = int(input("Enter a number between 1 and 99: "))


if(1 <= coins <= 99):
    # func call
    my_changes(coins)
else:
    print("You have entered a number that is outside of that range")
