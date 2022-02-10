word1 = input("Write 1.word: ").lower()
word2 = input("Write 2.word: ").lower()

set1 = {x for x in word1}
set2 = {y for y in word2}

a= list(set1&set2)
b= list(set1-set2)
c= list(set2-set1)

result= list()
for i in a,b,c:
    i.sort()
    x="".join(i)
    result.append(x)
print(result)

"""Write a program that takes in two words as input and returns a list containing three elements, in the following order
Shared letters between two words.
Letters unique to word 1.
Letters unique to word 2.
Each element of the output should have unique letters, and should be alphabetically sorted. Useset operations. The strings will always be in lowercase and will not contain any punctuation.
Example
Input1 sharp 
Input2 soap
Output ['aps', 'hr', 'o']"""