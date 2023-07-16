import random
while True:
    top_range = input('Enter a digit: ')
    try:
        top_range = int(top_range)
        if (top_range < 0):
             error = 'abc'
             error = int (error)
        break
    except ValueError:
        print ('Positive Numbers Only')

random_number = random.randrange (top_range)

while True:
    guess = input ('Enter a guess as a number: ')
    guess = int (guess)
    if (guess < random_number):
        print ('The number is higher, try again')
    elif (guess > random_number):
        print ('The number is smaller, try again')
    else:
        print (f'You guessed the number: {str(random_number)}')
        break

    



#does not include the number in the parameter, it's the absolute upper bound
#random_number = random.randrange(101)
#print (random_number)
