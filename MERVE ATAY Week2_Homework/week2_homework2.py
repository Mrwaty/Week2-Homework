a= int(input("Enter first number: "))       
b= int(input("Enter second number: "))

a=[x for x in range(1, a+1)]
print(a)

if b>0:
    list1=a[:(len(a)-b)]
    del a[:(len(a)-b)]
    a.extend(list1)
    print(a)

elif b<0:
    list2=a[:-b]
    del a[:-b]
    a.extend(list2)
    print(a)

"""
Write a program that takes two inputs; one of them is a list and the other is a number, 
and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative). 
Use wrap-around if an element is shifted beyond the end of the list, 
then continue to shift starting at the beginning of the list. 
Example 
Inputs [1, 2, 3, 4, 5], 2 
Output [4, 5, 1, 2, 3] 
Inputs [1, 2, 3, 4, 5], -2 
Output [3, 4, 5, 1, 2]
"""