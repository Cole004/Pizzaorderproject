print("Welcome to the pizza delivery")
size = input ("What's the size of pizza,Small,Medium or Large?\n")
add_pepperoni = input("Do you want to add pepperoni,Y or N\n")
add_cheese = input ("Do you want to add cheese,Y or N\n")
bill = 0 
if size == "S" or "s" :
  bill += 15
elif size == "M" or "m":
  bill += 20
else :
  bill += 25

if add_pepperoni == "Y" or "y" :
  if size == "S" or "s" :
    bill += 3
  else :
    bill += 4
if add_cheese == "Y" or "y" :
  bill += 2
  print(f"Your final bill is {bill}")
else :
  print(f"Your final bill is {bill}")   


