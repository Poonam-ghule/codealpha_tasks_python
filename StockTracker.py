import yfinance as yf
import pandas as pd

class PortfolioTracker:
    def __init__(self):  # Fixed the typo in __init__
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] <= 0:
                del self.portfolio[symbol]

    def get_portfolio_values(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            stock_info = yf.Ticker(symbol).history(period="1d")
            if not stock_info.empty:  # Check if data is available
                current_price = stock_info['Close'].iloc[-1]  # Fixed column name
                total_value += current_price * quantity
        return total_value

    def display_portfolio(self):
        print("Stock Portfolio:")
    
        for symbol, quantity in self.portfolio.items():
            print(f"{symbol}: {quantity}")

# Example usage
tracker = PortfolioTracker()
tracker.add_stock("AAPL", 10)
tracker.add_stock("GOOGL", 5)
tracker.display_portfolio()
print("Total Portfolio Value:", tracker.get_portfolio_values())
