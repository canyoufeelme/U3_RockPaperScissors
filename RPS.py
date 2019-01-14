import time
import random

print('-'*65)
print()
print('I am Game-Bot! ')
print('You will be playing Rock, Paper, Scissors against me today! I hope you are ready.')
print()
print()

print('-'*15)
print()
print('Rock')
print('Paper')
print('Scissors')
print()
print()

P1move = input('Please choose your move out of the 3 shown above: ')

print()
print('-'*15)


print('You picked: ' + P1move)

P2move = random.choice(["Rock", "Paper", "Scissors"])
print('Computer picked: ' + P2move)

if P1move == "Rock" and P2move == "Scissors":
	print('P1 Wins. Rock crushes scissors.')

if P1move == "Rock" and P2move == "Rock":
	print('P2 Wins. Rock crushes scissors.')

if P1move == "Rock" and P2move == "Rock":
	print('Tie')

if P1move == "Paper" and P2move == "Rock":
	print('P1 Wins. Paper covers Rock.')

if P1move == "Rock" and P2move == "Paper":
    print('P2 Wins. Paper covers Rock. ')

if P1move == "Paper" and P2move == "Scissors":
    print('P2 Wins. Scissors cuts paper.')

if P1move == "Paper" and P2move == "Paper":
    print('Tie')

if P1move == "Scissors" and P2move == "Scissors":
    print('Tie')

if P1move == "Scissors" and P2move == "Paper":
	print('P1 Wins. Scissors cuts paper.')





















































































