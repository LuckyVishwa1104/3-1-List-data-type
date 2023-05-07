#1. List data-type - collection of elem. separeted by commas in square braces.
#  List = [val_1,val_2,val_3, . . . ,val_n]

#1]. Creating and Declaring a list
''' syntax:
	list_name=[val1, val2, val3, --- , valn]
list_name= valid identifier
value=variables, input, output,
              expression, all data-types'''

#1. list of intergers 
list_int=[1,4,8,7,99,33,45,5,1]
print(list_int)
list_int1=[1,5,68,93,33,90]
print(list_int1)

#2. list of string
list_str=["India","is","my","country","jai hind"]
print(list_str)
string=["yes","eron","feed_back","alien_X"]
print(string)

#3. list of mixed data-type
mixed=[1,4,4.4,8.8-7j,"jello",0b1101,3,0o34]
print(mixed)
list_mix=["€€¥",2.3,3-7j,0b101,0x38AD,bool(23),True]
print(list_mix)

#4. list of mixed data
a,b=4,"pause"
mixed_2=[2.3,"oppo","@",8-3j,"###",5.12,a,b,6*a]
c,d,e=1,"etry",False
mix_list=["##",c,d,e,2+c,22,bool(9)]
print(mix_list)
print(mixed_2)

#5. complex list 
list_comp=["€#©",[1,2,2],7-77j,78-12,(1,a,b)]
print(list_comp)
complex_list=[3,3.-7j,[2,6,"jj",7.2,[23,88]],(1,99,"jj",[a,b,c,d]),{2,8,"jh","&&"}]
print(complex_list)