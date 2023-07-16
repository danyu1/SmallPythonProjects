List = [1, 2, 3]
Dict = {0: "A", 1: "B", 2: List}

for key in Dict:
    print (Dict[key])

#essentially like an array but with manual indexes lol
#for element in List:
 #   print (element)
print (List[0])

#example
customer = {
    "name": "John Smith",
    "age": 16,
    "is_verified": True
}

print (customer ["name"])
print (customer.get ("Name")) #avoids error
customer ["birthdate"] = "May 28 2006"
customer ["name"] = "Daniel Hernandez"
print (customer ["name"])
print (customer ["birthdate"])
