#6. List operations: there are two operation that can be performed on the list

#1]. Concatenation (+) - used to join two or more list
#1. join two list
list1=[1,3,5,7,9]
list2=[2,4,6,8,10]
list3=list1+list2
print(list3)

#2. join three list
list4=["joke","hii",3.1,8,"iop"]
list5=["a","e","i","o","u"]
list=list1+list4+list5
print(list)

#3. join undeclared list
list6=[0b101,"hii",(2,4,7),{"¶"}]
list7=list6+list2
print(list7+[5,67,777])

#2]. Repeatition (*) - used to repeate more than once.
#1. repete two times
list8=["¥","©","∆",5,6.7]
list9=list8*2
print(list9)

#2. repete three times
list10=["€",["~","^","®"],12,"holla"]
print(list10*3)

#3. repeting undeclared list
print([2,3,4,5]*3)
# repeating zero times delete all the elemnts of list
print([2,4]*0)
print(["#","$","@"]*1)
