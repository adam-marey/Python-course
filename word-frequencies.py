# Implement the build_dictionary() function to build a word frequency dictionary from a list of words.

# Ex: If the words list is:
# ["hey", "hi", "Mark", "hi", "mark"]

# the dictionary returned from calling build_dictionary(words) is:
# {'hey': 1, 'hi': 2, 'Mark': 1, 'mark': 1}

# The words parameter is a list of strings.
def build_dictionary(words):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer 
    # indicating that word's frequency.
    
    ''' Type your code here (remove the "pass" statement below) '''
    dic = {}
    for word in words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

# The following code asks for input, splits the input into a word list, 
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))