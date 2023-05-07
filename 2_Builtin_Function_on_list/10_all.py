#10. all() - return true value when all elem. are true or list is empty else return false value.
#Syntax:  all(list_name)   
true=[bool(1),True,6,bool("no"),bool(True)]
print(all(true))
empty=[]
print(all(empty))
# assigning to a variable
exp=[True and True,"fall",False or True,8,9-7j]
a=all(exp)
print(a)
print(all([bool("yy"),bool(True),True]))	
t=[True and True,bool(4),bool("uu")]
print(all(t),all([]))
# if any one value is false it return false 
d=[bool(2),True,bool("gg"),0,False]
print(all(d))
# when all values are false it return false
false=[0,False,bool(0)]
print(all(false))
# conditions for list all()
# True , True = True
# True , False / False , True = False
# False , False = False
# empty list = True
	  