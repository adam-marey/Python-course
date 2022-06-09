# "Supercalifragilisticexpialidocious"


# Write a program that:
# 1- Counts the letters.  Print the number of letters
# 2- That only prints the first 5 letters.
# 3- That concatenates Supercalifragilisticexpialidocious with "is something quite atrocious".
# 4- That breaks Supercalifragilisticexpialidocious into a list with three elements.
#   Create the list, then execute the list, concatenating it all back together into Supercalifragilisticexpialidocious.
#   Print the concatenated list.  There can be no white spaces.
# 5- Put your name into a list and print it.
# --------------------------------------------------------------
# program solution;

str = "Supercalifragilisticexpialidocious"

# 1
total_letters = len(str)
print("number of letters:", total_letters)  # this prints number of letters 

# 2
print(str[:5])

# 3
new_str = str + " " + "is something quite atrocious"
print(new_str) #should print new version of str

#4
list_of_elements = []
list_of_elements.append(str[0:int(len(str) / 3)])
list_of_elements.append(str[int(len(str) / 3): 2 * int(len(str) / 3)])
list_of_elements.append(str[2 * int(len(str) / 3):])

print(list_of_elements)

concatenated_str = ''
for element in range(len(list_of_elements)):
  concatenated_str += list_of_elements[element]
print(concatenated_str)


# 5
my_name = ["Sul", "Sam", "Adam"]
print(my_name[0])