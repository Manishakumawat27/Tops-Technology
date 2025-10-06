#write a python program to find the higest 3 values in a dictionary

dict={"math":90,"science":75,"ss":87,"hindi":77}

#store the top 3 values
top=[]

for values in dict.values():
    top.append(values )
    
    #list only top 3 values
    top=sorted(top,reverse=True)[:3]


print(top)    
