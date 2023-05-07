#11. any() - return True value when any one elem. is true or False when list is empty
'''  Syntax:
	   any(list name)  '''
g=[False,True,7,bool(6),7.2]
print(any(g)) 
k=[0,1,"jj",3,8.2,9+3j]
print(any(k))
# for empty list it return false value
empty=[]
print(any(empty))
# assigning to the variable
h=[7,8,9-7j,False,bool(0),0,{3,4.8}]
a=any(h)
print(a)
a,b=True,False
print(any([a,b,bool(7),True,1,0]))
# when all values are true it returns true 
true=[1,bool(8),6.9,"ty",True]
print(any(true))
# when all values are false it return false
false=[0,False,bool(0)]
print(any(false))
# condition for list any()
# True , True = True
# True , False / False , True = True
# False , False = False
# empty list = False 	 