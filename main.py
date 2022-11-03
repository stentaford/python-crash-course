

import random # import the ramdon number
counter_for_war = 0 #counter loop
boolean_while_game = True #while loop varable
boolean_while_war = True #while loop Varable
your_card = 0 #Random number from 1 to 10
opponent_card = 0 #Random number from 1 to 10
your_score = 0 #Player score
opponent_score = 0 #Computer score

#welcome Screen
print("=============================")
print("Python Game of War")
print("=============================")
user_input_play_game = str(input("Type PLAY and press ENTER:")) #ask user if the want to Play

# Computer war Game

if user_input_play_game == 'PLAY':
  print('\n')
 
  while(boolean_while_game == True):
    
    for counter_for_war in range(20): #for loop to iterate 20 times
      your_card = random.randint(0, 9)
      opponent_card = random.randint(0, 9)
    
      if(your_card > opponent_card):
        print("Your card:", your_card, "Opponent's card:", opponent_card)
        print("You won this round!")
        your_score += 2 # increment score by 2
       # print("War count ",counter_for_war,"score you ",your_score,"Opponent score ",opponent_score)
        str(input("Press ENTER to Contiune \n"))
        counter_for_war += 1 #increment by one each time
        boolean_while_game = False
     
      elif(your_card < opponent_card):
          print("Your card:", your_card, "Opponent's card:", opponent_card)
          print("Opponent won this round!")
          opponent_score += 2 # increment score by 2
          #print("War count ",counter_for_war,"score you ",your_score,"Opponent score ",opponent_score)
          str(input("Press ENTER to Contiune \n"))
          counter_for_war += 1 #increment by one each time
          boolean_while_game = False
        
      else:
        
        while(boolean_while_war == True):
          print("========WAR========")
          print("Your card:", your_card, "Opponent's card:", opponent_card,)
          print("========WAR========",'\n')
          your_card = random.randint(0, 9)
          opponent_card = random.randint(0, 9)
        
          if(your_card > opponent_card):
            print("Your WAR card:", your_card, "Opponent's WAR card:", opponent_card)
            print("You won this WAR!")
            your_score += 8 # increment score by 8
            #print("War count ",counter_for_war,"score you ",your_score,"Opponent score ",opponent_score)
            counter_for_war += 1 #increment by one each time
            boolean_while_war = False
     
          elif(your_card < opponent_card):
            print("Your WAR card:", your_card, "Opponent's WAR card:", opponent_card)
            print("Opponent won this WAR!")
            opponent_score += 8 # increment score by 8
           # print("War count ",counter_for_war,"score you ",your_score,"Opponent score ",opponent_score)
            str(input("Press ENTER to Contiune \n"))
            counter_for_war += 1 #increment by one each time
            boolean_while_war = False
          else:
            boolean_while_war == True
            str(input("Press ENTER to Contiune \n"))
            
            
      continue

  if(your_score > opponent_score):
    print("You Won! Play again?")
    print(your_score)

  else:
    print("You Lost! Play again")
    print(opponent_score)

else:
  print("Play again?")