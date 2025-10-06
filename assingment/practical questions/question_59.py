#write a python program to create a dictionary from a string
#note:track the count of the letters from the string

string="manishakumawat"

dict={}

for char in string:

    #check the  char is already exits or not
    dict[char]=dict.get(char,0)+1
print(dict)    
