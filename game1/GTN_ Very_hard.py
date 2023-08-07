import random
print( "welcome to my first game!")
name = input("Type yor name here: ")
playing=True
while playing:
    thenumber = random.randint(1,200)
    print("I think of a random number from 1 to 50")
    print("Are you smart enough to guess it?")
    tries = 0
    guess = 0
    while guess != thenumber:
        tries = tries + 1
        guess = int (input ("Split it out: "))
        if guess == 2011:
            print ("number = ",thenumber)
        elif guess > thenumber:
            print ("Oops!The number you guessed is bigger than the number I thought!")
        elif guess < thenumber:
            print ("Oops! The number you guessed is smaller than the number I thought!") 
    print ("Congracts ",name,"! You Guessed the number correctly in ",tries," tries !")
    q=input("Press Q to close the game OR press any to continue playing the game: ")
    if q=='Q':
        playing=False
    else:
        playing=True