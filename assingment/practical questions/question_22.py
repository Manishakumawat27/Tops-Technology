#write a python function to reverses a string if its length is a multiple of 4

text=input("Enter the strings::")

#check if the number is divided by 4c or  not
if len(text)%4==0:
    str=text[::-1]
else:
    str=text
    print(str)    