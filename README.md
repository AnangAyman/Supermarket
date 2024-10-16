# Point of Sale System Overview

This project is a Point of Sale (POS) system for a fictional supermarket, "Ayman's Supermarket." The program allows users to sign up, log in, browse inventory, add items to their cart, and complete purchases. Additionally, it includes functionalities for managers to manage inventory, including adding, deleting, and changing the prices of items.

## Features

- **User Signup and Login**: Allows customers to create an account and log in using a unique login code.
- **Shopping Cart Management**: Customers can add, view, and purchase items.
- **Inventory Management**: Inventory of items is categorized into Drinks, Snacks, Meat, Fruits, and Vegetables.
- **Manager Functions**: Includes options for managers to add, delete, or change the price of items.
- **Data Export/Import**: Customer data is stored in a CSV format.

### User Features
- **Customer Signup**: New customers can create an account by providing their name, email, and credit card number.
- **Customer Login**: Existing customers can log in using a unique login code generated during signup.
- **Shopping Cart**: 
  - Add items to the cart from various categories (Drinks, Snacks, Meat, Fruits, Vegetables).
  - View items in the cart, along with their quantity, price, and subtotal.
  - Remove or update items in the cart.
- **Checkout Process**: Calculate and display the total amount due and allow customers to complete their purchase.
- **Data Storage**: Customer information is stored and managed using a CSV file, allowing easy import and export of data.

### Manager Features
- **Manager Login**: Special login functionality for managers using a predefined manager code.
- **Inventory Management**: 
  - **Add New Items**: Add new items to any category in the inventory.
  - **Delete Items**: Remove items from any category.
  - **Update Prices**: Change the selling price of existing items.
- **Reports and Analytics**: Future enhancements planned to display customer data, total revenue, and most profitable items.

## Technologies Used

- Python Standard Library (`csv`, `os`, `random`)
- External Libraries: 
  - `pyfiglet`: For ASCII art generation.
  - `tabulate`: For displaying tables in a grid format.
  - `tkinter`: For GUI elements and message boxes.

## Required installation

- Make sure you have pyfiglet and tabulate installed
- or do so by executing pip install pyfiglet tabulate

## Usage
1. Run the Program: Run the main Python script: python main.py
2. Login or Signup:
    * Choose to log in as an existing customer or sign up as a new customer.
    * If signing up, provide your name, email, and a valid fictional 11-digit credit card number. You will receive a unique login code.
    * If logging in, just re-enter your unique login code that you have received before.
3. Shopping as a Customer:
    * Browse through different categories of items.
    * Add items to the cart, review your cart, and proceed to checkout.
    * View your net total and complete the purchase.
4. Manager Mode:
    * Log in using the manager code (M123).
    * Use various management functions to update the inventory, add new items, or delete items.

## Project Structure
* **Customer Class**: Represents a customer with methods to handle cart operations.
* **Item Class**: Represents an item in the inventory with properties such as name, quantity, and price.
* **Inventory Class**: Manages the inventory of items, allowing adding, removing, and modifying items.
* **Main Program**: Handles user and manager operations.

## Future Improvements
* Ensure the uniqueness of login codes.
* Add more robust error handling and input validation.
* Implement DBMS systems such as mySQL etc
* Make a more user friendly GUI
