#3. Traversing list - printing all element of list one by one, it can be done using loop.
'''  Syntax:
	    for variable in list_name:
	   	  body of loop  '''
# Examples
#1. printing element of list
list=[2,5,7,9,3,4]
# using for loop
for i in list:
	print(i)
print("end")
#2. printing english vowels
for i in ["a","e","i","o","u"]:
	print(i)
print("stop")
#3. displaying days in a week
week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for days in week:
	print(days)
print("week ended")
#4. incrementing elements of list by 5
list1=[1,3,5,7,9,11,13,15]
for n in list1:
	print(n+5)
print("done")
#5. traversing even no. from list
list2=[1,2,3,4,5,6,7,8,9,10]
for num in list2:
	if num%2==0:
		print(num)
print("end")