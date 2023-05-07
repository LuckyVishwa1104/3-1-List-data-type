#9. sort() - it arrange the element of list in increasing order.
# it accept no argument and elem. should be of same data-type.
''' Syntax :
	   list_name.sort()  ''' 

# sorting integers and float
print("1). Using sort() method : ") 
numbers=[2,6,1,0.8,6,8,52,7,8,2,False]
numbers.sort()
print(numbers)

# sorting bin, oct, hex
data=[0b101,0b111,0o25,0x6A,0x7D,0o77]
data.sort()
print(data)

# for other value it compare ascii value
# sorting alphabate
alph=["k","h","i","a","p","w","s",""]
alph.sort()
print(alph)

# sorting string value.
string=["hola","print","inpirll","aaa"]
string.sort()
print(string)

# sorting collection data-type - for collection-data type it compare first elem.
collect=[[78,9,7],[78,7,9]]
collect.sort()
print(collect)

#9. sorted() - is also used to arrange elem. of list in increasing order.
#Syntax:  sorted(list_name)
print("2). Using sorted() method :")
numbers=[2,6,1,0.8,6,8,52,7,8,2]
print(sorted(numbers))

# sorting bin, oct, hex
data=[0b101,0b111,0o25,0x6A,0x7D,0o77]
print(sorted(data))

# sorting alphabate
alph=["k","h","i","a","p","w","s"]
print(sorted(alph))  	

# sorting string value.
string=["hola","print","inpirll","aaa"]
print(sorted(string)) 	   	  	   	  	   	  