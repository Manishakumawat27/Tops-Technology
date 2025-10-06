#write a python script to sort(ascending and decending)a dictionary by values
dict1= {"Iphone15":85000,"Iphone 16":100000,"Iphone 12":75000}
        
asce=dict(sorted(dict1.items(),key=lambda item:item[1]))
print("Acending oreder is::",asce)

desc=dict(sorted(dict1.items(),key=lambda item:item[1],reverse=True))
print("Descendingorder is::",desc)
       
       