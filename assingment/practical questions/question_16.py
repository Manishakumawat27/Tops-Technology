#write a python program to count the number of characters
#(character frequency)in a string

str=input("Enter the string::")

if len(str)==1:
    print("please not enter the single char")
elif (char.isdigit()for char in str):
      print("please do no enter the digit")
else:
     count=[]
     for char in str:
          if char not in count:
               frequency=str.count(char)
               print(f""{char}:"{frequency}")
               count.append(char)