#write a python program to test whether a passed letter is a vowel or not

char=input("Enter the character::")
if len(char)!=1 or not char.isalpha():
    print("please enter the single alphabet and digit is not valid")
elif char.lower()in "aeiou":
    print(f"{char} is a vomel")
else:
    print(f"{char} is not a vomel")
        