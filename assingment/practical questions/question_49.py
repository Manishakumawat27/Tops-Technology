#write a python script to concatenate following dictionaries to create a new one


dict1={"name":"Manisha","surname":"kumawat"}
dict2={"age"==20,"course"=="bcom"}

dict3={}
for i in (dict1,dict2):
    dict3.update(i)

print(dict3)
