#7. append() - used to add one elem. at a time in last of a list.
''' Syntax:
	  list_name.append(element) 
element - input, output, variable, expression , all data-type  '''

plang=["php","html","css","cobol","swift"]	 
plang.append("python")
plang.append("java")
plang.append("c++")
print(plang)

# other element as element
list=[2,4,"g"]
list.append(2)
list.append(3-7j)
list.append([2,6,"hug"])
list.append(("#","©","&"))
list.append({2:3,5:6})
print(list)

# assigning to variable
listy=[3,6,8]
n=666666
listy.append(n)
print(listy)

# taking input
listy.append(int(input()))
print(listy)