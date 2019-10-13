import random
import math
score=0       # for score
tests=1       # for number of attempts, it is equal to 1 as if it is 0 and 'n' is inputted in line 18, still user has played once.
def game():
  global count
  global tests
  n=int(input("\nSelect your range i.e 0-___ "))
  a=int(input("Enter a random number between 0 and "+str(n)+"\n"))
  while(a>n):     #this loop is to ensure that the user input is always in the range
    print("invalid input please try again")
    a = input("Enter a random number between 0 and "+str(n)+"\n")
  b=random.randint(0,n)
  if a==b:
    print('\ncongrats!\n')
    score+=1
    print('\ncurrent score= ' + str(score))
  else:
    print('\nyou missed by ' + str(a-b) + '.')
    print('\ncurrent score= ' + str(score))         #displays current score
  c=input("Do You want to play again? If yes please press 1,otherwise press any key to exit")  #in the last version "y" had to be entered instead of y and thats confusing so since numbers are easier to understand
  if (c== 1):
    global tests
    game()
    tests+=1
  else:
    print('Game Over!')
    d=score/tests       #doesn't seem to work.
    print("Your Score= " +str(d)+ ".")

game()


