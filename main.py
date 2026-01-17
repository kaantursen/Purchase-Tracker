import datetime
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
db_name = os.getenv("DB_NAME")
client = MongoClient(mongo_uri)
db = client["budgetDB"]

print(f"Database successfully connected: {db.name}")
collection = db["expenses"]

while True:
    print("\n1. Add New Expense")
    print("2. List All Expenses and View Total")
    print("3. Exit")
    
    choice = input("\nSelect the operation you want to perform (1/2/3): ")

    if choice == "1":
        try:
            title = input("Enter expense title: ")
            price = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")

            expense_record = {
                "category": category,
                "title": title,
                "price": price,
                "created_at": datetime.now()
            }
            result = collection.insert_one(expense_record)
            print(f"Record successfully added! ID: {result.inserted_id}")
        except ValueError:
            print("!!! Error: You must enter only numbers for the amount.")
            
    elif choice == "2":
        all_expenses = list(collection.find())
        
        for expense in all_expenses:
            print(f"Title: {expense['title']} | Amount: {expense['price']} TL | Category: {expense['category']} | Date: {expense['created_at']}")
            
        total_amount = 0
        print("\n--- EXPENSE REPORT ---")
        for expense in all_expenses:
            amount = expense["price"]
            total_amount += amount
            print(f"• {expense['title']}: {amount} TL")
            
        print("-" * 20)
        print(f"YOUR TOTAL EXPENDITURE: {total_amount} TL")
        print("-" * 20)
        
    elif choice == "3":
        print("Exiting program... Have a good day!")
        break
