#write a python program that will return true if the two given integer values are
#equal or their sum or differnce is 5

num1=int(input("Enter number1::"))
num2=int(input("Enter number2::"))


#chcek the condition

if num1==num2 or num1+num2==5 or num1-num2==5:
    print("True")
else:
    print("please enter the valid input")
        