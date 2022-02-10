sentence=input("Write a sentence: ").lower()
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list1= [letter for letter in sentence if letter in alphabet ]
list1=sorted(list1)

list2=[]
for i in list1:
    count= list1.count(i)
    list2.append(count)

result= set(zip(list1,list2))

print(sorted(list(result)))

"""
Write a code snippet that inputs a sentence from the user, 
then uses a dictionary to summarize the number of occurrences of each letter. 
Ignore case, ignore blanks and assume the user does not enter any punctuation. 
Display a two-column table of the letters and their counts with the letters in sorted order.

"""