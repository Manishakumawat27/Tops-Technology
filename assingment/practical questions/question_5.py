#write a python program to get the factorial number of given number

num=int(input("Enter the number::"))
if num<0:
    print("Negative number is not efined")
elif num==0:
    print("Factorial of 0 is 1,please Enter validnumber")
else:
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(f"factorial of {num}is::",fact)
            
