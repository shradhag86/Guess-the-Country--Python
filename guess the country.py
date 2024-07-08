import random
countrylist =[ "India", "Singapore", "Spain", "Australia",
              "China","England","Switzerland", "Japan", 
               "Nepal","Germany","France"]

word = random.choice(countrylist).lower()

def win():
  print('''
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ////////// YOU WIN \\\\\\\\\\
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ''')  
  
def lose():  
  
  print('''
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  //////// GAME OVER \\\\\\\\\\
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ''')
  
print(''' 
*****************************
      GUESS THE COUNTRY
*****************************

Instructions:-
You have 5 lives . 
If you guess a wrong alphabet one lives gets taken up.
Guess the country before all lives are over.
''')


print("_ " * len(word))

chances = 5
correct = []
gameplay = True




# you guess the correct country or chances ==0

#game loop
while chances > 0 and gameplay:
    
    print()
    guess = input(" What is your guess: ").lower()
    

    if guess in word:
        print("Good Job: Remaining Chances: ", chances)
        correct.append(guess)
    else:
        chances -= 1
        print("Oh!! Try again, Remaining Chances: ", chances)



    for i in word:
        if i in correct:
            print(i," ", end="")
        else:
            print("_ ",end="")





    if set(word) == set(correct):
        gameplay = False


#ending
if chances > 0:
    win()
else:
    print()
    print("The correct word was ", word)
    lose()

