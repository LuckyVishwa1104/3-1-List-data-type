#2]. Using enumerate() function we can print both index and corresponding value.
'''  Syntax:
	     for var in enumerate(list_name):  '''
#1.displaying index and value
list3=[1,5,10,15,20,25,30]
for o in enumerate(list3):
	print(o)
#2. the h value is taken as tuple
list4=[1,2,3,4,5,6,7,8]
for h in enumerate(list4):
	print(h+(3,5))
#3. print days of week
week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for day in enumerate(week):
	print(day)
print("stop")
#4. print list of binary no.
list5=[0b000,0b001,0b010,0b011,0b100]
for k in enumerate(list5):
	print(k)
print("Program finished")