#write a python script to merge two python dictionaries

dict1={"name":"manisha","age":20}
dict2={"course":"data analytics","location":"parimal"}

print("dict1 is ::-",dict1)
print("dict1 is ::-",dict2)
dict3=dict1.copy()
dict3.update(dict2)
print("dict3 is ::-",dict3)


