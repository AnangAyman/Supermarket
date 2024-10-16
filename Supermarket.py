# -----------------------------------------------------------------------------
import random
import csv
import os
from pyfiglet import Figlet
from tabulate import tabulate

# * Class Variables

class items(object):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer(object):
    def __init__(self, name=None, creditCard=None, email=None, loginCode=None, transactionAmount=0, totalSpent=0, cart=None): 
        self.name = name 
        self.creditCard = creditCard 
        self.email = email
        self.loginCode = loginCode
        self.transactionAmount = transactionAmount
        self.totalSpent = totalSpent
        
        # Use an empty list if cart is not provided
        if cart is None:
            cart = []
        self.cart = cart
    
    def buy(self,item,quantity,price,subtotal):
        
        for entry in self.cart:
            if entry["Item(s)"] == item:
                
                entry["Quantity"] += quantity 
                entry["Subtotal"] += subtotal
                return 
            
        # If item doesn't exist, add it as a new entry
        self.cart.append({"Item(s)": item, "Quantity": quantity, "Price":  price, "Subtotal" : subtotal})
    
    def pay(self):
        subtotal = 0
        for entry in self.cart:
            subtotal += entry["Subtotal"]
        
        header = ["Nett Total"]
        tableData = [[subtotal]]
        table = tabulate(tableData, headers=header, tablefmt="grid")
        print("\nHere are your nett total(s): ")
        print(table)
    
    def checkCart(self):
        if len(self.cart) == 0:
            print("Your cart is empty!")
        else:
            print("Items in your cart: ")
            table = tabulate(self.cart, headers="keys", tablefmt="grid")
            print(table)

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        self.quantity += amount

    def __repr__(self):
        return f"{self.name} (Quantity: {self.quantity}, Price: {self.price})"


class Inventory:
    def __init__(self):
        self.items = {
            "Drinks": [
                Item("Coca Cola", 100, 10),
                Item("Sprite", 100, 9),
                Item("Beer", 100, 12),
                Item("Wine", 100, 40),
                Item("Water", 100, 3),
            ],
            "Snacks": [
                Item("Oreo", 100, 10),
                Item("Chips", 100, 12),
                Item("Candy", 100, 5),
                Item("Popcorn", 100, 18),
                Item("Lollipop", 100, 12),
            ],
            "Meat": [
                Item("Beef", 100, 60),
                Item("Pork", 100, 40),
                Item("Lamb", 100, 50),
                Item("Chicken", 100, 30),
                Item("Vegan Meat", 100, 80),
            ],
            "Fruits": [
                Item("Apple", 100, 8),
                Item("Banana", 100, 7),
                Item("Durian", 100, 18),
                Item("Cherry", 100, 18),
                Item("Grape", 100, 13),
            ],
            "Vegetables": [
                Item("Carrot", 100, 6),
                Item("Asparagus", 100, 7),
                Item("Cabbage", 100, 4),
                Item("Onion", 100, 6),
                Item("Potato", 100, 9),
            ],
        }

    def add_item(self, category, name, quantity, price):
        if category in self.items:
            new_item = Item(name, quantity, price)
            self.items[category].append(new_item)
        else:
            print(f"Category '{category}' does not exist.")

    def display_items(self):
        category_options = []
        for i, category in enumerate(self.items, start=1):
            category_options.append([i, category])
        
        print("Category Options:")
        print(tabulate(category_options, headers=["No", "Category"], tablefmt="grid"))
        
    def display_category(self, category):
        if category in self.items:
            table_data = [[i + 1, item.name, item.quantity, item.price] for i, item in enumerate(self.items[category])]
            headers = ["#", "Item(s)", "Quantity", "Price"]
            print(f"{category}:")
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
            print()
        else:
            print(f"Category '{category}' does not exist.")

# --------------------------------- Miscellaneous Functions ----------------------------------------
def enterToContinue():
    input("\nPress enter to continue...")

# ------------------------- Printing Functions --------------------------------
def printHeader(login_Code):
    name = getUserName("customers.csv", login_Code)
    print(f"\n|----------Welcome to Ayman's Supermarket, {name}----------|")
    print('1. Shopping Cart\n2. Purchase items\n3. Exit')
    choice = int(input('Enter the number of your choice : '))
    return choice

# ---------------------------------- Signup ---------------------------------------------
def signup ():
    name = input("Enter your full name : ").lower()
    creditCard = input("Enter your credit card: ")
    while len(creditCard) != 11:
        creditCard = input("Enter a CORRECT 11 digit credit card information: ")
    
    email = input("Enter your email address: ")
    loginCode = random.randint(100000,999999) #! Future Update : Make sure login code is unique
    print(f"Your Login Code: {loginCode}")
    enterToContinue()
    previousTransactionAmount = 0
    a = Customer(name,creditCard,email,loginCode,previousTransactionAmount) # Make a new customer object, then write it to the database

    with open("customers.csv", 'a') as file:
        file.write(f"{name},{creditCard},{email},{loginCode},{previousTransactionAmount}\n")


# --------------------------------- Login Functions --------------------------------
def checkLoginCode(csv_file_path, login_code):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['LoginCode'] == login_code:
                return True
    return False

def getUserName(csv_file_path,login_code):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['LoginCode'] == login_code:
                return row['Name']
    return False

def login():
    repeat = True
    while repeat  != False:
        loginCode = input("\nEnter Your Login Code: ")

        # * Manager Login
        if loginCode == "M123" : 
            managerProgram()
            break
        
        # * User Login
        elif checkLoginCode("customers.csv", loginCode) == True :
            userProgram(loginCode)
            break
        else:
            print("\nPlease enter your login code correctly or sign up if you don't have one.")
            print("1. Re-enter\n2. Sign up\n3. Forgot login code")
            option = int(input("What do you want to do: "))
            os.system("clear")
            if option == 1:
                pass
            elif option == 2:
                signup()
            elif option == 3:
                name = input("Enter your name: ").lower()
                with open("customers.csv","r") as file:
                    csv_reader = csv.DictReader(file)
                    for row in csv_reader:
                        if name == row["Name"]:
                            print(f"Your login code is : {row['LoginCode']}")


def login_page():
    os.system("clear")
    print("\n|---------Ayman's Supermarket----------|")
    option = int(input("1. Login\n2. New Customer\n3. Exit\nEnter : "))
    return option

# --------------------------------- User Program ----------------------------------------
inventory = Inventory()
def userProgram(login_Code):
    global inventory
    activeCustomer = Customer(loginCode= login_Code)
    while True:
        choice = printHeader(login_Code)
        if choice == 1:
            os.system('clear')
            activeCustomer.checkCart()
            enterToContinue()
            os.system('clear')
        elif choice == 2:
            os.system('clear')

            inventory.display_items()
            categoryChoice = int(input("Which category do you want to buy from?: "))
            os.system('clear')

            match categoryChoice:
                case 1:
                    category_name = "Drinks"
                case 2:
                    category_name = "Snacks"
                case 3:
                    category_name = "Meat"
                case 4:
                    category_name = "Fruits"
                case 5:
                    category_name = "Vegetables"
                case _:
                    print("Invalid choice. Please select a valid category.")
                    continue  # Skip the rest of the loop if invalid
                    # or use break if it's inside a loop
                


            # Validate item choice
            while True:
                os.system("clear")
                # Display the selected category and get the item choice
                inventory.display_category(category_name)
                itemChoice = int(input("Which item number do you want to buy?: ")) - 1  # Convert to zero-based index
                itemQuantity = int(input("How much do you want to buy? "))
                if 0 <= itemChoice < len(inventory.items[category_name]):
                    selected_item = inventory.items[category_name][itemChoice]
                    
                    # Check if enough quantity is available
                    if selected_item.quantity >= itemQuantity:
                        # Update inventory and process the purchase
                        selected_item.update_quantity(-itemQuantity)
                        activeCustomer.buy(selected_item.name, itemQuantity, selected_item.price, selected_item.price * itemQuantity)
                        enterToContinue()
                        os.system('clear')
                        break
                    else:
                        print(f"Insufficient quantity available for {selected_item.name}.")
                        enterToContinue()
                else:
                    print("Invalid item choice. Please select a valid item number.")
                    enterToContinue()


        elif choice == 3:
            os.system('clear')
            activeCustomer.checkCart()
            activeCustomer.pay()
            enterToContinue()
            os.system("clear")
            figlet = Figlet()
            figlet.getFonts()
            figlet.setFont(font='doom')
            print(figlet.renderText("Thank You For Shopping"))
            enterToContinue()
            break


# --------------------------------- Manager Program --------------------------------------
def printManagerOptions():
    print(f"Manager Commands: ")
    commands = [
        ["1", "Change Selling Price"],
        ["2", "Add Items"],
        ["3", "Delete Items"],
        ["0", "Exit"]
    ]
    
    print(tabulate(commands, headers=["Command", "Description"], tablefmt="grid"))

def changePrice():
    global inventory
    while True:
        os.system("clear")
        inventory.display_items()
        categoryChoice = int(input("Which category do you want to change the price?: "))
        os.system('clear')
        match categoryChoice:
            case 1:
                category_name = "Drinks"
                break
            case 2:
                category_name = "Snacks"
                break
            case 3:
                category_name = "Meat"
                break
            case 4:
                category_name = "Fruits"
                break
            case 5:
                category_name = "Vegetables"
                break
            case _:
                print("Enter the proper category choice!")
    
    # Display the selected category and get the item choice
    inventory.display_category(category_name)

    itemChoice = int(input("Which item number do you want to change the price?: ")) - 1  # Convert to zero-based index
    if 0 <= itemChoice < len(inventory.items[category_name]):
        selected_item = inventory.items[category_name][itemChoice]
        newPrice = int(input("What price do you want it to be changed into?: "))
        while newPrice < 0:
            os.system("clear")
            print("The new price cant be a negative value!")
            newPrice = int(input("What price do you want it to be changed into?: "))
        selected_item.price = newPrice
        print("\nItem's price has been changed")
        enterToContinue()

def addItems():
    global inventory
    while True:
        os.system("clear")
        inventory.display_items()
        categoryChoice = int(input("Which category do you want to add an item to?: "))
        os.system('clear')
        match categoryChoice:
            case 1:
                category_name = "Drinks"
                break
            case 2:
                category_name = "Snacks"
                break
            case 3:
                category_name = "Meat"
                break
            case 4:
                category_name = "Fruits"
                break
            case 5:
                category_name = "Vegetables"
                break
            case _:
                print("Enter the proper category choice!")

    # Display the selected category and get the item choice
    itemName = input("Enter the new item's name: ")
    itemQuantity = int(input("Enter the new item's quantity: "))
    itemPrice = int(input("Enter the new item's price: "))
    inventory.add_item(category_name,itemName,itemQuantity,itemPrice)
    tableData = [[itemName, itemQuantity, itemPrice]]
    header = ["Item Name", "Item Quantity", "Item Price"]
    table = tabulate(tableData, headers=header, tablefmt="grid")
    print(table)
    print("Item has been added")
    enterToContinue()

def delItems():
    global inventory
    while True:
        os.system("clear")
        inventory.display_items()
        categoryChoice = int(input("Which category is the item you want to delete?: "))
        os.system('clear')
        match categoryChoice:
            case 1:
                category_name = "Drinks"
                break
            case 2:
                category_name = "Snacks"
                break
            case 3:
                category_name = "Meat"
                break
            case 4:
                category_name = "Fruits"
                break
            case 5:
                category_name = "Vegetables"
                break
            case _:
                print("Enter the proper category choice!")

    # Display the selected category and get the item choice
    inventory.display_category(category_name)
    itemChoice = int(input("Which item number do you want to delete?: ")) - 1
    selectedCategory = inventory.items[category_name]
    del selectedCategory[itemChoice]
    print("\nItem has been deleted")
    enterToContinue()

def managerProgram():
    while True:
        os.system("clear")
        printManagerOptions()
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                changePrice() # * Done
            case 2:
                addItems()
            case 3:
                delItems()
            case 0:
                break
            case _:
                pass  # Handle invalid choice

# -------------------------------- MAIN PROGRAM -------------------------------------------
def main():
    os.system('clear')
    exit = False
    while exit != True:
        option = login_page()

        if option == 1: # Login
            os.system('clear')
            login()

        elif option == 2: # Signup
            os.system('clear')
            signup()

        elif option == 3: # Exit
            print("Thank You For Using The Program")
            enterToContinue()
            break
    return

if __name__ == "__main__":
    main()