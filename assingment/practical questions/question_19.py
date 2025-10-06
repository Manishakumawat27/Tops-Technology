#write a python program to count the occurrences of each word in a given sentence

text=input("Enter the stringds::")

#convert the string into lowercase because of the case sensitive language
lower=text.lower()

#split the string into words
split=lower.split()
#print(split)

#create the dictionary to store the words
word_count={}

#count the words
for words in split:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

#print the words occurence
for word,count in word_count.items():
    print(word,count)          