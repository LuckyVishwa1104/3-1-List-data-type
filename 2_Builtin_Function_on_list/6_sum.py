#6. sum() - return the sum of all elem. of list
# For sum function the list should contain element of same data-type.
''' Synatx:
	   sum(list_name,value) 
	   value is added to sum of list.  '''
# valid only for numeric and bool data-type
  
# int, float, complex 
list=[2,4,7,9,1,6]
print(sum(list))
list2=[2.3,7.2,0.001,7.88]
print(sum(list2))
list3=[8-7j,-4.6-8.9j,7-0.03j]
print(sum(list3))
# bin, oct, hex
listb=[0b101,0b001,0b111,0b1010]
print(sum(listb))
listo=[0o23,0o701,0o12]
print(sum(listo))
listx=[0xA1,0x23D,0x9EF,0x23AE]
print(sum(listx))
# boolean
listbool=[bool(87),True,False,bool("jj")]
print(sum(listbool))
# mixed data-type
listm=[7.8,6,0b101,0xA5,0o53,6-7j,bool(88)]
print(sum(listm))
# assigning to variable
b=55
lst=[5,6,6,78,b]
a=sum(lst)
print(a,sum([7,9.8,1,0b101]))
# along with first parameter of sum second can also be used with operators.
print(sum(lst,b))
list33=[10,20,30]
print(sum(list33,40))