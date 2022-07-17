# Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase.
#  The output should include the input character and use the plural form, n's, if the number of times the characters appears is not exactly 1.

# input:
# n Monday

# output:

# 1 n

ch=input()

index=0

for i in range(len(ch)):
    if(ch[i]==' '):
        index=i
        break

str=ch[index+1:len(ch)]

ch=ch[:index]


count=0

for i in range(len(str)):
    if (str[i]==ch):
        count=count+1


if(count==1):
    print("{} {}".format(count, ch))
else:
    print("{} {}'s".format(count, ch))