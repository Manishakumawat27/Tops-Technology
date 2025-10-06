#write a python program to combine values in  python list of dictionaries
#sample data:[{'item':'item1','amount':400},{'item':'item2','amount':300},o{'item':'item1','amount':750}]
#Expected output
#counter({'item1:1150,'item2:300})

from collections import Counter
sample_data=[
    {'item':'item1','amount':400},
    {'item':'item2','amount':300},
    {'item':'item1','amount':750}
]

#store the value in counter
dict=Counter()
#print(Sample_data)

for i in sample_data:
    dict[i['item']]+=i['amount']

print(dict)    





