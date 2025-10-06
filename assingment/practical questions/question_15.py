#write a python program to calculate ythe length of  a string

#str="hello cutie"
str=input("Enter the strings::")

#remove the space
if str.replace("","").isalpha():
    print("length of string is::",len(str))
else:
    print("Enter the only string not a digit")
        