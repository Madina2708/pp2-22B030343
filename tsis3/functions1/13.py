import random
import histo

histo.hist([1,2,3])

def AskForGuess():
    while True:
         guess = input('> ') 
 
         if guess.isdecimal():
             return int(guess)  
         print('Please enter a number between 1 and 20.')

print('Guess the Number...')
print()
secretNumber = random.randint(1, 20)  
print('I am thinking of a number between 1 and 20.')
 
for i in range(10): #количество шансов
     print('You have {} guesses left. Take a guess.'.format(10 - i))
 
     guess = AskForGuess()
     if guess == secretNumber:
      break
      if guess < secretNumber:
         print('Your guess is too low.')
     if guess > secretNumber:
         print('Your guess is too high.')

if guess == secretNumber:
 print('Congrats!!!You guessed my number!')
else:
     print('Game over. The number I was thinking of was', secretNumber)
