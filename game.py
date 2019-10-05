import random
import math
count=0       # for score
tests=1       # for number of attempts, it is equal to 1 as if it is 0 and 'n' is inputted in line 18, still user has played once.
def game():
  global count
  global tests
  n=int(input("\nSelect your range i.e 0-___ "))
  a=int(input("Enter a random number between 0 and "+str(n)+"\n"))
  b=random.randint(0,n)
  if a==b:
    print('\ncongrats!\n')
    count+=1
    print('\ncurrent score= ' + str(count))
  else:
    print('\nyou missed by ' + str(a-b) + '.')
    print('\ncurrent score= ' + str(count))         #displays current score
  c=str(input("Do You want to play again?(Y/N) "))   # if user inputs 'y' or 'Y', game() is called again
  if c=='Y' or c=='y':
    global tests
    game()
    tests+=1
  else:
    print('Game Over!')
    d=count/tests       #doesn't seem to work.
    print("Your Score= " +str(d)+ ".")

game()


