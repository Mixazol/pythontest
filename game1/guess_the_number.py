import random
print( "welcome to my first game!")
name = input("Type yor name here: ")
thenumber = random.randint(1,50)
print("I think of a random number from 1 to 50")
print("Are you smart enough to guess it?")
guess = 0
while guess != thenumber:
    guess = int (input ("Split it out: "))
    if guess > thenumber:
        print ("Oops! Your guessed number is bigger than the number I thought!")
    if guess < thenumber:
        print ("Oops! Your guessed number is smaller than the number I thought!") 
print ("Congracts ",name,"! You Guessed the number correctly!")