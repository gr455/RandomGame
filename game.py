import random
def game():               
  score=0                     #for score
  number_of_attempts=1      #for number of attempts
  isPlaying = True          #for the first run.

  range_of_guess=int(input("Select a range(0-___) for guessing. "))
  print("Remember, the bigger number, the higher your potential score! ")

  while isPlaying:
    user_guess=int(input("Enter a random number between 0 and "+str(range_of_guess)+"(both inclusive)."))
    computer_guess=random.randint(0,range_of_guess)       #computer generates a random number in this way
    
    if user_guess==computer_guess:
      print('Congrats! You got it right!')
      print('The probability of this is ' + str(1/(range_of_guess+1)))    #adds probability for a sense of satisfacton of player
      score+=range_of_guess           # prevents free riders using 0 always
      print('Current score= ' + str(score))
    
    else:
      print('You missed by ' + str(user_guess-computer_guess) + '!')
      print('Your current score: ', score)         
    
    play_again = input("Do You want to play again?(Y/N) ")   
    if play_again == 'Y' or play_again == 'y':
      number_of_attempts += 1
    else:
      isPlaying = False

  print('Game Over!')
  final_score=score/number_of_attempts             
  print("Your Score: ",final_score)            

game()

