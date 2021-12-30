# Name: Maleeha Mirza
# Date: March 31, 2021
# Name: SelfCheckout 
# Purpose of program: To allow the user to self-checkout their items at a grocery store. 

# Creates and initializes global variables so that they could be accessed in the functions.
askStartProgram = ""
addItem = ""
items = []
itemQuantities = []
itemPrices = []
removeItem = ""
askPaymentMethod = ""
cashChange = ""

# Introduces the program to the user in detail. 
def introduce_program(): 

  print(" Welcome to Food Basics Self-checkout! " .center(55,"~"))
  print("")
  print("You will have to enter all your product names, the quantity (how many of each product), and their unit prices. For instance, if you have oranges as one of your products and the amount of oranges is 6, you enter oranges as the item and 6 as the quantity.")
  print("")
  print("Then, the program asks for the price where you have to enter the price for each orange/orange package, indicated under the product's barcode. You repeat this process for all the items that you have. There is also no need for you manually typing the $ dollar sign in front of the prices as the program will do it for you.")
  print("")
  print("*Please keep in mind that when entering the quantity, prices, and cash change, please only enter numbers!")

  global askStartProgram
  while not askStartProgram.startswith("Y"):
    print("")
    askStartProgram = input("Do you want to start? Enter Y for yes: ").capitalize()

    if askStartProgram.startswith("Y"): 
      print("")
      print("Here we go:")
      print("".center(12, "-"))
      print("")
      print("FOOD BASICS SELF CHECKOUT".center(35))
      self_checkout()

# Asks the user if they would like to remove any items and removes items accordingly. 
def remove_items():
  global removeItem
  print("")
  while not removeItem.startswith("N"):
    removeItem = input("Do you want to remove any item? Enter Y for yes or N for no: ").capitalize()
    print("")
    
    # Outputs the current shopping cart of the user to help them figure out which item they want to remove.  
    if removeItem.startswith("Y"): 
      print("Here is your shopping cart so far:")
      print("")
      i = 0
      while i<len(items): 
        for x in range(len(items)):
          i = i + 1
          print(f'{str(i) + "." :<1} {str(items[x]) + ":":>5}{str(itemQuantities[x]) + " for ":>7}{str("$" + str(itemPrices[x]) + " each."):>5}')
      
      print("")
      askRemoveItem = int(input("Which item would you like to remove? Enter the number of the item indicated on the left of the item in the shopping list: "))
  
      items.pop(askRemoveItem-1)
      itemPrices.pop(askRemoveItem-1)
      itemQuantities.pop(askRemoveItem-1)
      remove_items()
    
# Asks the user how many of each item they have and repeats the question if the user types in characters other than integer numbers. 
def ask_quantity(): 
  quantity = input("Quantity: ")
  quantity.isnumeric()
  if quantity.isnumeric() == False: 
    print("")
    print("Please enter only whole numbers!")
    ask_quantity()
  else:
    itemQuantities.append(int(quantity))

# Asks the user for their items, quantity, and prices for each item. Also,  it asks the user if they would like to add another item. 
def self_checkout():
  
  print("".center(35, "~"))
  item = str(input("Item: ")).capitalize()
  items.append(item)
  ask_quantity()
  pricePerItem = float(input("Price: $"))
  itemPrices.append(pricePerItem)
  print("")

  global addItem
  while not addItem.startswith("D"):
    addItem = input("Add item? Enter Y for yes or D for done entering items: ").capitalize()
    print("")
    if addItem.startswith("Y"):
      self_checkout()
    elif addItem.startswith("D"):
      remove_items()
      payment_method()

# Performs calculations of the subtotal, tax, and total cost of all the items the user checked out. Additionally, it calculates the prices of each item after multiplying it by quantity. 
def calculations():
  
  multiplyPricesByQuantity = []
  for i in range(len(itemQuantities)): 
    multiplyPricesByQuantity.append(float(itemQuantities[i] * itemPrices[i]))

  subtotal = sum(multiplyPricesByQuantity)
  salesTax = float(0.13* float(subtotal))
  global total
  total = '{:.2f}'.format(float(subtotal + salesTax ))

# Rounds the total cost to a cash total that meets Canada's rounding guidelines.
def cash_rounding():
  calculations()
  global total
  total = str(total)
  if total.endswith("1") or total.endswith("6"):
    total = float(total)-0.01
  elif total.endswith("2") or total.endswith("7"):
    total = float(total) - 0.02
  elif total.endswith("3") or total.endswith("8"):
    total = float(total) + 0.02
  elif total.endswith("4") or total.endswith("9"):
    total = float(total) + 0.01
  elif total.endswith("5") or total.endswith("0"):
    total = float(total)
  
# Asks the user for their choice of payment method. It also asks the user how much cash they would like to pay and calculates the cash change if they chose cash as their payment option.
def payment_method(): 
  global askPaymentMethod
  
  print("")
  print(f'{"1. Debit Card":<18} {"2. Credit Card":<7} {"3. Cash":>12} ')

  while not (askPaymentMethod == 1 or askPaymentMethod ==2 or askPaymentMethod ==3):
    print("")
    askPaymentMethod = int(input("How would you like to pay today? Enter the number of your payment choice from the above options: "))
    if askPaymentMethod == 3: 
      calculations()
      cash_rounding()
      print("")
      global total
      print("Your total is " + "${:.2f}".format((total)) + ".")
      print("")
      global cashAmount
      cashAmount = float(input("How much cash will you pay today? (Enter only whole numbers or decimal numbers) $"))
      while cashAmount<total: 
        print("Sorry that is not enough cash. Please enter an amount equal to or higher than the total given.")
        print("")
        cashAmount = float(input("How much cash will you pay today? $"))
      global cashChange
      cashChange = '${:.2f}'.format(float(cashAmount - total))

  final_receipt() 

# Outputs the final receipt to the user. 
def final_receipt(): 
  global askPaymentMethod
  global total
  print("")
  print("Here is your receipt:")
  print("")
  print(f'{"".center(30, "=")}')
  print("FOOD BASICS".center(30))
  print(f'{"".center(30, "=")}')
  print(f'{"Item:":<13}{"Price":>16}')
  print("")

  multiplyPricesByQuantity = []
  for i in range(len(itemQuantities)): 
    multiplyPricesByQuantity.append(float(itemQuantities[i] * itemPrices[i]))

  # Outputs the items, quantities, and total price after multiplying it by the quantity. Also formats the total price to correctly align with other costs below it in a column. 
  for x in range(len(items)):
    if multiplyPricesByQuantity[x]>=10:
      print(f'{"(" + str(itemQuantities[x]) + ")":>2}{items[x]:<20}{"${:.2f}".format(multiplyPricesByQuantity[x]):>1}')
    else: 
      print(f'{"(" + str(itemQuantities[x]) + ")":>2}{items[x]:<21}{"${:.2f}".format(multiplyPricesByQuantity[x]):>1}')
    print(f'{itemQuantities[x]:<2}{"@" :<2}{"${:.2f}".format(itemPrices[x]):>2}')

  print(f'{"".center(30, "-")}')
  subtotal = sum(multiplyPricesByQuantity)
  print(f'{"SUBTOTAL":>15}{"${:.2f}".format(subtotal):>14}')
  salesTax = float(0.13* float(subtotal))
  print(f'{"GST/HST":>14}{"${:.2f}".format(salesTax):>15}')
  total = '${:.2f}'.format(float(subtotal + salesTax ))
  print(f'{"TOTAL":>12}{total:>17}')

  # Outputs the total payment amount that the user enters depending on if they chose debit, credit, or cash as payment option. If they choose cash, it also outputs the change. 
  if askPaymentMethod == 3: 
    calculations()
    cash_rounding()
    print(f'{"CASH TOTAL":>17}{"${:.2f}".format(total):>12}')
    print(f'{"CASH TEND":>16}{"${:.2f}".format(cashAmount):>13}')
    print(f'{"CHANGE DUE":>17}{str(cashChange):>12}')
  elif askPaymentMethod == 1: 
    print(f'{"DEBIT TEND":>17}{total:>12}')
  elif askPaymentMethod ==2: 
    print(f'{"CREDIT TEND":>18}{total:>11}')

  # Outputs the number of items that the user checks out. 
  print("")
  print((" # ITEMS SOLD " + str(len(items)) + " ").center(30, "*"))
  print(f'{"".center(30, "=")}')
  print("")
  print("")

# Outputs the final goodbye message.
def final_goodbye_message():
  print(" THANK YOU FOR SHOPPING WITH US ".center(40,"~"))
  print("")
  print("Have a great day!".center(40,))

# *** Functions end here! ***

# These functions execute the entire program.
introduce_program()
final_goodbye_message()
