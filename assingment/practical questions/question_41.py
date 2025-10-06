#write a python program to check whether a list contains a sub list
lst=[10,20,30,40,50,60]
lst1=[10,20]
if lst1 in lst:
    print("list contain sublist")
else:
    print("list not contain sublist")



lst=[10,20,30,40,50,60]
lst1=[10,20]

found=False
n=len(lst1)

for i in range(len(lst)-n+1):
    if lst[i:i+n]==lst:
        found=True

        break

if found:
    print("list contains sublist")
else:
    print("list does not contain sublist")
        