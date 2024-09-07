# OrderApp - Assignment 2.1

## Overview
OrderApp is a simple command-line application that manages customer information and allows customers to purchase products. The app stores customer details, product data, and shopping cart information in JSON format and enables easy management of orders and balances. 

## Features
1. **Customer Registration**: 
   - New customers can register by providing their ID, name, email, and address.
   - The system ensures that customer IDs are between 1001 and 9999 (auto-generated).
   - If a customer already exists, they can log in using their email.
   - Email addresses must be unique.

2. **Product Selection**: 
   - Once logged in, customers can view a list of available products (from pdata.json).
   - Customers can select products using their product ID (pid) and specify the quantity.

3. **Shopping Cart Management**:
   - Customers can add multiple products to a shopping cart.
   - Shopping carts can be saved in customer ID json file.
   - Each cart is saved as a unique JSON file in the data’s directory.

4. **View Shopping Carts**:
   - Customers can view their saved shopping carts along with the total price.
   - The customer’s balance owed is calculated from the carts.

5. **Payment System**:
   - Customers can pay for a shopping cart, and the corresponding cart file is deleted to update the balance owed.

## Requirements
- **JSON Files**: 
   - Customer information is stored in `customer.json`.
   - Product data is loaded from `pdata.json`.
   - Shopping cart data is saved in individual JSON files within customer-specific directories.
   
- **Menu-driven Interface**: 
   - The application provides an intuitive menu to guide customers through various options such as registration, product selection, shopping cart management, and payment.

## How to Run
1. Clone or download the project.
2. Ensure you have Python installed.
3. Navigate to the project folder and run the application with:
   ```bash
   python index.py
   ```
4. Follow the menu prompts to perform operations.

## File Structure
```bash
OrderApp/
│
├── index.py      # Main application file
└── data/        # Folder for storing customer shopping cart data
    │
    ├──  cart/
       └── {customerID}.json  # Each customer has a directory for their carts
       └── {customerID}.json
       └── {customerID}.json
    ├──  customer.json   # Stores customer details
    └──  pdata.json        # Contains product information


```
