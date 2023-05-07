#5. min() - return the minimum element of list.
# for this function the list should contain elements of same data-type
''' Syntax :
	   min(list_name)  '''
num=[1,2,5,6,7,0.2]
print(min(num))
list=[1,1.1,1.11,1.111]
print(min(list))
# for other than numeric data it compaires ascii value.
alph=["a","h","A","u","c"]
print(min(alph))
# by assigning value to variable
lst1=["@","#","$","_","%","+","-"]
lst2=[2*5,5,5-7,89-1]
a,b=min(lst1),min(lst2)
print(a,b)
# using argument
print(min([2,4,5,7.8]))
  	   	   	   	   	   