#write a python function that ttakes two lists and returns true if they have at least one common member

lst=[123,456,789]
lst2=[854,123,785]

def check(lst1,lst2):
    for item in lst1:
        if item in lst2:
            return True
        return False
    print(check(lst1,lst2))
    