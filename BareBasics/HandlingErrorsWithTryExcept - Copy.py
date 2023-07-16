try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print (age)
except ValueError:
    print ("Invalid Error")
except ZeroDivisionError:
    print ("Invalid Age Value")
