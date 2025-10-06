#write a python program to add "in" at the end of a given string(length
#should be atleast 3).if the given string already ends with 'ing' then add'ly'
#instend if the string length of the given string is less than 3,leave it unchanged

text=input("Enter the string::")

if len(text)<3:
    str=text
elif text.endswith("ing"):
    str=text+"ly"
else:
    str=text+"ing"

    print(str)    
