#12. insert() - used to add an elem. to particular index without chaning the pre-existing list.
'''' Syntax:
	  list_name.insert(index,value)  '''
num=[4,5,9,3,8,2]
print(num)
num.insert(-1,"ooooo")
num.insert(1,67)
num.insert(2,0b1011)
num.insert(5,0xA3F)
num.insert(6,-8-9.2j)
num.insert(7,7*3)
print(num)
# if index is more than last index of list then it will add to last index
list=[7,8.9,"hh"]
print(list)
list.insert(6,7.9)
list.insert(7,[2,0b101,"j"])
list.insert(3,"holy")
list.insert(4,8*2)
list.insert(9,"iiii")
print(list)
	  	  	  