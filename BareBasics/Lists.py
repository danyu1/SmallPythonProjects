a = [1, 2, 4]
a.append ("THERES NO WAY")
print (a)
#append a new list within the already existing list
a.append ([1,2])
print (a)

#delete the last element in the array
a.pop()
print (a)

#insert element at given index
a.insert(0, 10)
print (a)

#checks if a element is in a list
print (50 in a)

#returns the index of a passed integer
#print (a.index(50))

#sorts numbers and string in descending order
a.pop()
a.sort ()
#descending order, strings go at the front because they have a higher hex value?
a.reverse ()
print (a)

a2 = a.copy ()
a2.append ("THIS DOESN'T AFFECT THE PREVIOUS LIST")
print (f"{a} copy: {a2}")