#Delcare Variable for while loop
menu_var = str("")  
#Declare List
grocery_list =["apple","banana","cherry"] 
#Declare Variable to just pause the program
hold_var = str("")      
#Declare variable to remove item
remove_item = str("")
#import OS
import os

#While user don't enter q
while(menu_var != 'q'):  
  
  # Menu
  print("-----------------------------------------------------")
  print("                  Grocery List")
  print("-----------------------------------------------------")  
  print("1) View Grocery List")
  print("2) Remove Groceries")
  print("-----------------------------------------------------")
  
  #Menu choice
  menu_var= str(input("\nEnter a number option and press ENTER or type 'q' to quit: "))

  #Print groceries
  if (menu_var == "1"):
    
    #Print list
    print("\n")
    for x in grocery_list:
      print(x)
    else:
      hold_var = input("\nPress Enter to countiue")
      os.system('clear') #clear

  #Remove groceries from list
  elif(menu_var == "2"): 
      remove_item = input("\nEnter in the grocery item and press ENTER:")

      if remove_item in grocery_list:
        grocery_list.remove(remove_item)
        
        #Print list
        print("\n")
        for x in grocery_list:
          print(x)
        else:
          hold_var = input("\nPress Enter to countiue")
          os.system('clear') #clear
          
      else:
        print("\n item not in list try again!")
        hold_var = input("\nPress Enter to countiue")
        os.system('clear') #clear
        
else:
  os.system('clear') #clear
  print(" Program ended!")