#write a python program to get the fibonacci series of given range

#define the range
start=10
end=100

#initialize first two fibonacci number

a,b=0,1

#generate fibonacci number in range
while a<=end:
    if a>=start:
        print(a,end="")
    a,b=b,a+b 