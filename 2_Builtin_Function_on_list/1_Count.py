# There are Different methods or builtin functions avaiable that perform operation on list.
#1. Count() - return max. count of particular element.
'''  Syntax :
	    list_name.count(element)
element - input, output, variable, expression , all data-type .  
Appicable with - list, tuple, string, sequence.  '''
nums=[1,2,3,2,4,3,3,5,3,6,7,6,7,8,7,7,7]
print(nums.count(3))
print(nums.count(6))
a,b=nums.count(2),nums.count(7)
print(a,b)
c=nums.count(4)
print(c,nums.count(8))
# it returns 0 value when other than list element are passed
print(nums.count(99))
print(nums.count("kk"))