#2. Accessing element of list - to retrive particular elements of list.
# index - position of element in sequence.
''' using the index of element we can access the element
syntax:
	list_name[index]  '''

list=[2,4,7,8,5,9]
print(list[2])
print(list[0])
print(list[1+2]) # 1+2 =3

#1) using positive index (Left to Right) -      0 to (n-1).
list_1=[2,6,8,7.4,11,17-3j,23,42]
print(list_1[0])
print(list_1[3])
a=list_1[5]
print(a)
print(list_1 [7])
print(list_1[2+4])

#2) using negative index (Right to Left) :      -1 to -n.
list_2=[3,"hii",0x23A,bool(None),78-6j,"pop"]
print(list_2[-1])
print(list_2[-4])
print(list_2[-3])
print(2+list_2[-6])
print(list_2[-6]+list_2[-4])

#3) using slice ' : ' - starting to ending index.
# using slice operater we can multliple elements
'''list_name=[starting_index : ending_index : step size]'''
list_3=[9,7.3,"hil",[5,7,9],7-8j,0o23,(7,8,9)]
print(list_3[0:4:2])
print(list_3[2:7])
print(list_3[-4:-1])
print(list_3[-7:-1])
print(list_3[1:2])
print(list_3[-2:-1])
# the first value is 0 by default
print(list_3[:5])
# when last value is not assigned it goes to last value
print(list_3[4:])
# it will print entire list
print(list_3[:])
# third argument act as increment
print(list_3[0:7:2])
