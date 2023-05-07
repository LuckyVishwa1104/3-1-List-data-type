#14. list() - convert other data-type or sequence into list.
#Synatx :  list(sequence or data) 

animal="horse"
print(list(animal))
num=2,4,5,8,9
print(list(num))

#sequence can be of numeric, bool ,string, and collection data-type
numeric=4,0.4,-3+5j,0b101,0o45,0x5A1E
print(list(numeric))
boolean=True,bool(8),False,bool(0)
print(list(boolean))

# mixed data-type
string="df","tt","ttl",[78,8,8],(9,8)
print(list(string))

# string is converted into list
string1="happybirthday"
l=list(string1)
print(l)

# collection data-type is directy coverted to string
tuple=(2,7.8,"hh",9-7j,0b101,["&","*","@"])
print(list(tuple))
set={"a",8,"e","i","o",38,8,8,(3,3.3)}
a=list(set)
print(a)
dictionary={2:4,3:9.0,"e":"vowel","list":7}
print(list(dictionary))
