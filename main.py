import json
import random
from datetime import datetime
import os
import time
#searched a couple of things up but you can read the readme.md for more info
class Stock:
    def __init__(self, symbol, initial_price):
        self.symbol = symbol
        self.base_price = initial_price
        self.price = initial_price

    def update_price(self):
        change = random.uniform(-1, 1)
        self.price = self.base_price * (1 + change / 25)

class StockMarket:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock):
        self.stocks[stock.symbol] = stock

    def get_stock_price(self, symbol):
        return self.stocks.get(symbol).price if symbol in self.stocks else None

    def update_prices(self):
        for stock in self.stocks.values():
            stock.update_price()

    def print_prices(self):
        for symbol, stock in self.stocks.items():
            print(f"Stock {symbol}: Price ${stock.price:.2f}")

class User:
    def __init__(self, name, password, balance=10000.0):
        self.name = name
        self.password = password
        self.balance = balance
        self.portfolio = {}

    def buy_stock(self, market, symbol, quantity):
        price = market.get_stock_price(symbol)
        if not price:
            print(f"Stock '{symbol}' not found.")
            return

        total_cost = price * quantity
        if total_cost > self.balance:
            print(f"Insufficient funds to buy {quantity} shares of '{symbol}'.")
            return

        self.balance -= total_cost
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
        print(f"{self.name}: Bought {quantity} shares of '{symbol}' for ${total_cost:.2f}. Balance: ${self.balance:.2f}")

    def sell_stock(self, market, symbol, quantity):
        if symbol not in self.portfolio or self.portfolio[symbol] < quantity:
            print(f"You don't have enough shares of '{symbol}' to sell.")
            return

        price = market.get_stock_price(symbol)
        if not price:
            print(f"Stock '{symbol}' not found.")
            return

        total_sale = price * quantity
        self.balance += total_sale
        self.portfolio[symbol] -= quantity
        print(f"{self.name}: Sold {quantity} shares of '{symbol}' for ${total_sale:.2f}. Balance: ${self.balance:.2f}")

    def print_portfolio(self):
        print(f"{self.name}'s Portfolio:")
        if not self.portfolio:
            print("You don't own any stocks.")
        else:
            for symbol, quantity in self.portfolio.items():
                print(f"{symbol}: {quantity} shares")

    def save_data(self):
        data = {
            "name": self.name,
            "password": self.password,
            "balance": self.balance,
            "portfolio": self.portfolio
        }
        try:
            os.makedirs("users", exist_ok=True)
            with open(f"users/{self.name}_data.json", "w") as f:
                json.dump(data, f, default=str)
        except IOError:
            print(f"Error saving data for {self.name}")

def signup_or_login():
    while True:
        choice = input("Do you want to (L)ogin or (S)ignup? ").upper()
        if choice == 'S':
            user = signup()
            if user:
                return user
        elif choice == 'L':
            user = login()
            if user:
                return user
        else:
            print("Invalid choice. Please enter 'L' or 'S'.")

def signup():
    name = input("Enter a username: ")
    password = input("Enter a password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return None

    try:
        with open(f"users/{name}_data.json", "r") as f:
            print(f"User '{name}' already exists. Please choose another username.")
            return None
    except FileNotFoundError:
        user = User(name, password)
        user.save_data()
        print(f"User '{name}' created successfully!")
        return user
    except IOError:
        print("Error accessing user data.")
        return None

def login():
    name = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open(f"users/{name}_data.json", "r") as f:
            data = json.load(f)
            if data["password"] == password:
                user = User(data["name"], data["password"], data["balance"])
                user.portfolio = data["portfolio"]
                print(f"Welcome back, {user.name}!")
                return user
            else:
                print("Incorrect password.")
                return None
    except FileNotFoundError:
        print(f"User '{name}' not found.")
        return None
    except IOError:
        print("Error accessing user data.")
        return None

if __name__ == "__main__":
    user = signup_or_login()

   
    market = StockMarket()
    market.add_stock(Stock("AAPL", 250.0))
    market.add_stock(Stock("GOOGL", 190.0))
    market.add_stock(Stock("MSFT", 460.0))
    market.add_stock(Stock("AMZN", 200.0)) 
    market.add_stock(Stock("TSLA", 250.0)) 


    try:
        while True:
            market.update_prices()
            market.print_prices()
            action = input("Choose an action: (B)uy, (S)ell, view (P)ortfolio: ").upper()

            if action == 'B':
                symbol = input("Enter the symbol of the stock you want to buy: ").upper()
                quantity = int(input("Enter the quantity of shares you want to buy: "))
                user.buy_stock(market, symbol, quantity)
            elif action == 'S':
                symbol = input("Enter the symbol of the stock you want to sell: ").upper()
                quantity = int(input("Enter the quantity of shares you want to sell: "))
                user.sell_stock(market, symbol, quantity)
            elif action == 'P':
                user.print_portfolio()
            else:
                print("Invalid input. Please enter 'B', 'S', or 'P'.")

            time.sleep(1)  
    except KeyboardInterrupt:
        print("\nProgram stopped. Saving data...")
        user.save_data()
