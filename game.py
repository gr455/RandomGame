import random
import math
count=0
tests=1
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
    print('\ncurrent score= ' + str(count))
  c=str(input("Do You want to play again?(Y/N) "))
  if c=='Y' or c=='y':
    global tests
    game()
    tests+=1
  else:
    print('Game Over!')
    d=count/tests
    print("Your Score= " +str(d)+ ".")

game()


