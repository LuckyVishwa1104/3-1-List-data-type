#4. max() - return the maximum element of list.
# for this function the list should contain element of compairable data-type

''' Syntax :
	   max(list_name)  '''

num=[1,2,3,4,5,6,7,7,8]
print(max(num))
num1=[1,1.1,1.11,1.111]
print(max(num1))

# for other than numeric data-type it consider ascii value
alph=["a","j","u","#+","2"]
print(max(alph))

# assiging to variable
lst1=[2,2.2,2.22,3.3]
lst2=[7-8,6-9,3+2]
a,b=max(lst1),max(lst2)
print(a,b)

# using as argument
print(max(["#","@","_","%"]),max([7,8,9]))
