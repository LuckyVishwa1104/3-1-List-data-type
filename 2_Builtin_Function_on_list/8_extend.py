#8. extend() - used to add more than one elem. at the last of list.
''' Synatx:
	   list_name.extend(argument) 
argument - can only be string, list, tuple, set, dict '''

list=[5.5,6.6,7.7]
list.extend([8.8,9.9])
print(list)

# adding string element
strg=["a","e","i"]
strg.extend("ou")
print(strg)

# adding list element
even=[2,4,6,8,10]
even.extend([1,3,5,7,8])
print(even)

# adding tuple element
str=["ibm","ifa","ipl","pkl"]
str.extend(("rbi","www","http"))
print(str)

# adding set element.
city=["pune","nagar","kota"]
city.extend({"mumbai","jaipur","noida"})
print(city)

#for dictionary only key value is added
num=[1,2,3]
d={4:16,5:25,6:36}
num.extend(d)
print(num)
	   	   