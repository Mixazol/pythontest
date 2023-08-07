import random
print( "Καλωσορίσατε στο πρωτο μου παιχνιδι!")
name = input("Γραψε το ονομα σου εδω: ")
playing=True
while playing:
    thenumber = random.randint(1,50)
    print("Θα σκεφτω εναν αριθμο απο το 1 εως το 50")
    print("Εισαι αρκετα εξυπνος για να τον βρεις?")
    tries = 0
    guess = 0
    while guess != thenumber:
        tries = tries + 1
        guess = int (input ("Γραψε τον αριθμο που σκεφτηκες εδω: "))
        if guess == 2011:
            print ("Αριθμος = ",thenumber)
        elif guess > thenumber:
            print ("ουπς! Ο αριθμος που μαντεψες ειναι μεγαλυτερος απ'αυτον που σκεφτηκα !")
        elif guess < thenumber:
            print ("Ουπς! Ο αριθμος που μαντεψες ειναι μικροτερος απ'αυτον που σκεφτηκα !") 
    print ("Συγχαρητηρια ",name,"! Μαντεψες σωστα τον αριθμο που σκεφτηκα σε ",tries," προσπαθιες !") 
    q=input("Πατα το Q για να βγεις απο το παιχνιδη Η πατα οτιδηποτε αλλο για να συνεχισεις: ")
    if q=='Q':
        playing=False
    else:
        playing=True      