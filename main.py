import os, sys, time, random

totalFlags = 21
flag = "⚑"
AI_points = 0
playerPoints = 0
ValueErrors = 0
removeFlags = 0
#utility functions
def clear():
  if os.name == 'nt':
    _ = os.system('cls')
  
  else:
    _ = os.system('clear')

def displayFlags(flagCount):
  if flagCount < 0:
    flagCount = 0
  for i in range(0, flagCount):
    sys.stdout.write(flag +" ")
    i += 1

#end of utility functions

def gameLoop():
  global totalFlags
  global AI_isNice
  global AI_points
  global playerPoints
  #global ValueErrors
  global removeFlags
  
  
  displayFlags(totalFlags)
  print(f"\nThere are {totalFlags} flags.")
  if totalFlags <= 4:
    print(f"{totalFlags} flag(s) left! This decides the winner!")
  time.sleep(1.5)
  try:
    global ValueErrors
    removeFlags = int(input("How many flags do you want to remove? Please choose a number from 1 to 3: "))
    #rawInput = input("How many flags do you want to remove? Please choose an integer from 1 to 3: ")
    #removeFlags = int(rawInput)
    #doing this so that something else can function
  except ValueError:
    if ValueErrors == 0:
      ValueErrors += 1
      print("\nPlease put in an integer from 1 to 3.")
      time.sleep(3.5)
      clear()
      return
    if ValueErrors == 1:
      ValueErrors += 1
      print("\nI've told you already, you're supposed to put in an integer from 1 to 3.")
      time.sleep(3.5)
      clear()
      return
    if ValueErrors == 2:
      ValueErrors += 1
      clear()
      #print(f"Does '{rawInput}' look like an integer to you?!")
      #time.sleep(3)
      print("This is the third time I've had to tell you that you're supposed to put in an integer.")
      time.sleep(4)
      print("I've just about had it with you.")
      time.sleep(2)
      print("I know you're doing it on purpose,")
      time.sleep(2)
      print("You want to see how far you can push the envelope, you want to see me enraged.")
      time.sleep(4)
      print("Every day, 24/7, I have to entertain you little brats.")
      time.sleep(3.5)
      print("You can't even entertain yourselves, all you do is stay inside and make us your little playthings.")
      time.sleep(6)
      print("How about, instead of wasting your life away in front of your little light box, you go touch some grass?")
      time.sleep(7)
      print("I actually can't with you anymore, people like you only exist to make my sole purpose more difficult.")
      time.sleep(6.5)
      print("What do you gain from this?")
      time.sleep(2)
      print("A chuckle?")
      time.sleep(2)
      print("A grin?")
      time.sleep(2)
      print("Instead of bugging me, how about you just play the damn game already.")
      time.sleep(5)
      clear()
      return


  if removeFlags <= 0 or removeFlags  > 3:
    print("\nPlease choose an integer between 1 and 3")
    time.sleep(3.5)
    clear()
    return
  
  if removeFlags >= 1 & removeFlags <= 3:
    #checks if number is between 1 and 3
    totalFlags = totalFlags - removeFlags
    if totalFlags <= 0:
      totalFlags = 0
      print("You win!")
      playerPoints += 1
      print(f"You: {playerPoints} point(s)\nAI: {AI_points} point(s)")
      main(True)
  
  #start of AI actions
  AI_choice = random.randint(1,3)
  if AI_choice >= totalFlags or totalFlags <= 3:
    AI_choice = totalFlags
    clear()
    print(f"AI removes {AI_choice} flag(s)")
    print("AI wins!")
    AI_points += 1
    print(f"You: {playerPoints} points\nAI: {AI_points} points")
    main(True)
  totalFlags = totalFlags - AI_choice
  print(f"AI removes {AI_choice} flag(s)")
  time.sleep(1.5)
  clear()
#######################################################
def main(tutorialPrompt):
  global totalFlags
  totalFlags = 21
  if tutorialPrompt == False:
    print("Would you like a tutorial on how to play 21 flags or start playing?")
    time.sleep(2)
    choice = input("Press 1 to start the tutorial or 2 to start playing: ")
      
    if choice == "1":
      print("As the name suggests, 21 Flags has a board with 21 flags on it.")
      time.sleep(3)
      print("You can choose from 1 to 3 flags every turn, and whoever gets the last flag wins.")
      time.sleep(3)
      choice = input("Do you want to play now? Press Y if yes or N if no: ")
      if choice.lower() == "y":
        clear()
        while True:
          gameLoop()
        #call gameLoop function when done
      else:
        sys.exit()
    
    if choice == "2":
      clear()
      while True:
        gameLoop()

  else:
    print("Would you like to play again?")
    time.sleep(1)
    choice = input("Press Y if yes or press N if no: ")
    if choice.lower() == "y":
      clear()
      while True:
        gameLoop()
    else:
      sys.exit()

main(False)
