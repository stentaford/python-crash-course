# I used Encapsulation for this Challenge

chromosome_number = int(0) # Delcare Var

# Display
print("=====================================================")
print("Chromosome Count Analysis")
print("\n=====================================================")

# Define Classes
class Person:
  
  def __init__(self,chromosome):
    self.chromosome = chromosome

  def chromosome_func(self): # Display what a person chromosome is
    
    if (self.chromosome == 44):
      
      print("\nThis individual is a female")
      print("This individual does not have Down Syndrome.")
      print("This individual does not have Turner's Syndrome")

    if (self.chromosome == 45):
      
      print("\nThis individual's sex is unknow, additional karyotyping required.")
      print("This individual does not have Down Syndrome.")
      print("This individual may have Turner's Syndrome")

    if (self.chromosome == 46):

      print("\nThis individual is a male")
      print("This individual does not have Down Syndrome.")
      print("This individual does not have Turner's Syndrome")

    if (self.chromosome == 47):

      print("\nThis individual's sex is unknow, additional karyotyping required.")
      print("This individual may have Down Syndrome.")
      print("This individual does not have Turner's Syndrome")

chromosome_number = Person(int(input("Enter in the number of chromosomes and press ENTER: ")))
chromosome_number.chromosome_func()
