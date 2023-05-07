#3. len() - return the length of list i.e. total.no of elements of list
''' Syntax :
	  len(list_name)  
list name - valid variable   '''

list=[1,2,3,4,5,6,7,8,9,10]
print(len(list))
char=["¢","@","#","$","©","∆"]
print(len(char))

# assiging to a variable
J,K,Q,A="jocker","king","queen","ace"
cards=[2,3,4,5,6,7,8,9,J,K,Q,A]
a=len(cards)
print(a)

# using list as argument
print(len([2,4,6,8,10]))
d=[9,9,9,9,9,9]
print(len(d),len([9,9,9,9,9,9,9]))    	  	  