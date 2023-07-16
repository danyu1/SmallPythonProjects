def greet_user (first_name, last_name):
    print (f"Hello There {first_name} {last_name}!")
    print ("Welcome Aboard")


print ("Start")
greet_user ("Daniel", "Hernandez")
#keyword arguments improve the readibility of the code in particular situations
greet_user (last_name = "Hernandez", first_name = "Daniel")
print ("Finish")