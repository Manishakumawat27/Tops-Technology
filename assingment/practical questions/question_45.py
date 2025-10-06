#write a python program to unzip a list of tuples into individual lists

#create the list into tuple
list_tuple=[(10,20),(30,40)]

#create two different list and "*" operator is used for unpacking list of tuples
list1,lis2=zip(*list_tuple)

#convert into list
print("convert into list1::",list(list1))
print("convert into list2::",list(list2))

