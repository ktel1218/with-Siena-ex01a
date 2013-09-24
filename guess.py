from random import randrange 

#Greeting!
name = raw_input("Hey what's your name ")
print "Hey, %s, thats a name. Let's play a game. I'm guessing a number" % name
print "between 1 and 100, try to guess what it is" 

#Random number!
random_number = randrange(1,101)

not_won = True

#Guess!
while not_won:
    
    guess = int(raw_input("> "))

    if guess < random_number:
        print "Too low, try again."
    elif guess > random_number:
        print "Too high, try again."
    else:
        print "Yeah you won."
        not_won = False