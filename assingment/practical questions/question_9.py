#write python program that swap two number with temp variable andwithout temp variable

num1=int(input("enter num1::"))
num2=int(input("enter num2::"))
print("before the swap number")
#before the swap

print("num1 is:",num1)
print("num2 is:",num2)
#with the temp variable
temp=num1
num1=num2num2=temp
#after the swap number
print("after the swap number")
print("num1 is:",num1)
print("num2 is :",num2)
print("******************************")
#swap without temp variable
a=int(input("Enter A:"))
b=int(input("Enteer B:"))
print("before the swap number")
print("B is:",b)
b=b+a
a=b-a
b=b-a
print("after the swap number")
print("A is :",a)
print("B is :",b)
