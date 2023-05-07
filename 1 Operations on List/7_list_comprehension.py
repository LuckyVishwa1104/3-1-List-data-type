#7. List Comprehension - creating new list from existing list
# writing general code inside the square brackets
# Syntax : [expression for item in range]
list=[x for x in range(1,6) ]
print(list)
list2=[(y+1) for y in (2,4,6,8,10)]
print(list2)

#1. using if with list comp.
even=[e for e in range(1,21) if e%2==0]
print(even)
odd=[o for o in range(1,11) if o%2!=0]
print(odd)

#2. using nested if 
list3=[x for x in even if x%5==0 if x%2==0]
print(list3)
print([n for n in range(1,11) if n%2==0 if n%2==1])

#3. using if else
list4=["even" if k%2==0 else "odd" for k in range(1,16)]
print(list4)
age=int(input("Enter age : "))
list5=["adult" if age>=18 else "child"]
print(list5)

#4. using nested loop
list6=["*" for i in range(1,6) for j in range(i)]
print(list6)
# first loop is outer loop.
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
list7=[[row[i] for row in mat ] for i in range(len(mat[0]))]
print(list7)
#5. neted loop
print([(x,y,z) for x in [1,2,3] for y in [4,5,6] for z in [7,8,9]])

