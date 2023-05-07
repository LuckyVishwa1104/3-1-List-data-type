# There are two more ways by which we can traverse a list i.e. using range function and enumerate function.
#1]. Using range() function
'''  Syntax:
	    for var in range(list_length):   '''
#1. display element of list
list=[1,2,3,4,5]
for i in range(0,5):
	print(list[i])
#2. display using length of list
for i in range(len(list)):
	print(list[i])
#3. Using while loop
j=0
while j<5:
	print(list[j])	
	j=j+1	
k=0
while k<len(list):
	print(list[k])
	k=k+1
print("stop")
#4. increment element by 1
list1=[1,2,3,4,5,6,7]
for i in range(len(list1)):
	print(list1[i]+1)
print("end")
