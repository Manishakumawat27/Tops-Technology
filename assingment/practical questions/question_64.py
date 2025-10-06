#write a python function that check whether a passed string is palindrome or not

def palindrom(s):
    return s==s[::-1]

print(palindrom("manisha"))
print(palindrom("priyanka"))

    