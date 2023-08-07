import random
print( "welcome to my first game!")
name = input("Type yor name here: ")
thenumber = random.randint(1,200)
print("I think of a random number from 1 to 50")
print("Are you smart enough to guess it?")
tries = 0
guess = 0
while guess != thenumber:
    tries = tries + 1
    guess = int (input ("Split it out: "))
    if guess > thenumber:
        print ("Oops!The number you guessed is bigger than the number I thought!")
    if guess < thenumber:
        print ("Oops! The number you guessed is smaller than the number I thought!") 
print ("Congracts ",name,"! You Guessed the number correctly in ",tries," tries !")