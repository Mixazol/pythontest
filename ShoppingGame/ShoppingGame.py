# 3-01.py
import random

money = 15
shoppingList = []

def buy(productName,price):
    global money
    msg = 'Would you like to buy a '+ productName+' for '+  str(price)+' euros? '
    t = input (msg)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
    elif t.lower() == 'yes':
        if money >= price:
            money = money - price
            print ('Congrats! You just bought a', productName, 'for', price, 'euros.\nYour remaining bank balance is', money, 'euros')
            shoppingList.append(productName)
        else:
            print ('Your balance is not enough to buy this product')
    elif t.lower() == 'no':
        print ('You didn\'t buy a', productName, 'for', price, 'euros.\nYour remaining bank balance is', money, 'euros')

while money >= 0:
    print ('You have' , money, 'euros')
    print ('You are going to buy some things from the store')
    buy('toothpaste',2)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('A kilo of potatoes',3.5)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('A kilo of tomatoes', 2.7)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('toothbrush set', 3.2)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('milk', 2.1)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('Loaf of Bread',1.2)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('cheese',3)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('Slices of bread',2.5)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('feta cheese',4.1)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('chocolate',2)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('chips',2.3)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('Toilet paper (ew)',3)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    buy('Ham',2.4)
    if money <= 0:
        print('Your balance is ',money,'! Game over!')
        break
    break
print ('\nYou finished your shopping!\nYour remaining bank balance is ', money, 'euros.\nYour shopping list is:',shoppingList)
