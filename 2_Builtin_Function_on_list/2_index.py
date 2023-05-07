#2. index () - return the positive index of element
''' Syntax :
	   list_name.index(element) 
element - input, output, variable, expression , all data-type 
Appicable with - list, tuple, string, sequence.  ''' 
alph=["a","b","g","k","b","o","p","x","v","b"]
print(alph.index("a"))
print(alph.index("b"))	   
print(alph.index("x"))
a,b=alph.index("o"),alph.index("k")
print(a,b)
c=alph.index("v")
print(c,alph.index("v"))	

# when same elem. present more then once it return the index of first appearence only.
print(alph.index("b"))	 

# if elem. is not present it raises value error
# print(alph.index("#"))  --> value error