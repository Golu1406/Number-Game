import random
while True:
  c=int(input('''Enter your choice
  1) Start
  2) End\n'''))
  if c==1:
    computer_score=0
    Your_score=0
    print("Game start")
    for i in range(5):
      n=int(input("Enter the number between 1 to 100"))
      print("user Input: ",n)
      com=random.randrange(1,101)
      print("Computer Input: ",com)
      if n>com:
        print("User Win the round",n)
        Your_score=Your_score+1
        print("Your score", Your_score)
        print("Computer score", computer_score)
      elif com>n:
        print("Computer Win the game",com)
        computer_score=computer_score+1
        print("computer score", computer_score)
        print("user score", Your_score)
      else:
        print("Round is draw: ",n,com)
        Your_score=Your_score+1
        print("Your score: ", Your_score)
        computer_score=computer_score+1
        print("Computer score: ", computer_score)
    if computer_score>Your_score:
      print("computer win the game", computer_score)
      print("You loose the game", Your_score)
    elif Computer_score<Your_score:
      print("You win the game", Your_score)
      print("Computer lost the game", computer_score)
    else:
      print("game is draw")
      print("Your_score", Your_score)
      print("computer score", computer_score)
  else:
    print("existing...")
    break
        
          