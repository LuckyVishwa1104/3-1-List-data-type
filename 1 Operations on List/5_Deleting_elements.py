#5. Deleting elements of list - removing element of the list 
# deletion is carried out by pop, del, remove functions.

#1]. pop( ) - used to delete element at particular index.
#Syntax:   list_name.pop(index)
print("pop()_function")	             
# deleting other element except vowels      
vowels=["a",3,"e","p","i","t","o","y","u",7.8]
print(vowels) 	          
vowels.pop(1)
vowels.pop(2)
vowels.pop(3) 
vowels.pop(-1) 
vowels.pop(-2)
print(vowels)
# deleting odd no.
even=[1,2,3,4,5,6,7,8,9,10]
print(even)
even.pop(0)
even.pop(1)
even.pop(-6)
even.pop(-4)
even.pop(-2)
print(even)
# when no argument is passed (-1) is taken as default.
even.pop()
print(even)

#2]. remove( ) - used to delete a particular elelment.
#Syntax :  list_name.remove(value)
print("remove()_function")	    
# remove bird from list
animals=["lion","tiger","cheeta","parrot","hyena","deer","zebra","peacock","monkey","crow"]
animals.remove("parrot")
animals.remove("peacock")
animals.remove("crow")
print(animals)
# remove characters from list
data=[2,3.24,"@",0b110,"boll","$",True,0x1A2,"jack_sequerq","π",(9,8,7)]
data.remove("@")
data.remove("π")
data.remove("$")
print(data)
# when element is present more than one time, the first matching elem. get removed
lisr=[2,3,4,56,4,7,888,9]
lisr.remove(4)
print(lisr)

#3]. del function - used to delete two or more element at a time.
#Syntax :  del list_name[start : end index] 
# delete all even no.
prime=[1,3,5,7,2,4,6,8,11,13,17]	   
del prime[4:8]
print(prime)
prime=[1,3,5,7,2,4,6,8,11,13,17]	   
del prime[-7:-3]
print(prime)
even=[1,2,3,4,5,6,7,8,9,10]
del even[0:9:2]
print(even)
# starting index is 0 by default
odd=[1,3,5,7,9,11,13,15,17]
del odd[:4]
print(odd)
# also print last index
odd=[1,3,5,7,9,11,13,15,17]
del odd[5:]
print(odd)
# no argument = delete entire list
odd=[1,3,5,7,9,11,13,15,17]
del odd[:]
print(odd)