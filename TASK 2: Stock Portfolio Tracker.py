# Stock Portfolio Tracker
# Hardcoded stock prices (simplified values for demo)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 1200,
    "MSFT": 300,
    "AMZN": 3500
}

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("-" * 40)

total_value = 0.0
portfolio = []  # List to store (symbol, quantity, value) tuples

# Loop to add stocks
while True:
    symbol = input("Enter stock symbol (or 'done' to finish): ").upper().strip()
    if symbol == 'DONE':
        break
    
    if symbol not in stock_prices:
        print(f"Stock '{symbol}' not found in available stocks. Skipping.")
        continue
    
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity must be a positive integer. Skipping.")
            continue
    except ValueError:
        print("Invalid quantity. Please enter a number. Skipping.")
        continue
    
    # Calculate value for this stock
    price = stock_prices[symbol]
    value = price * quantity
    total_value += value
    
    # Add to portfolio
    portfolio.append((symbol, quantity, value))
    print(f"Added {quantity} shares of {symbol} at ${price} each. Subtotal: ${value:,.2f}")

# Display summary
print("\n" + "=" * 40)
print("Portfolio Summary:")
print(f"{'Stock':<8} {'Quantity':<10} {'Value':<12}")
print("-" * 30)
for symbol, quantity, value in portfolio:
    print(f"{symbol:<8} {quantity:<10} ${value:,.2f}")
print("-" * 30)
print(f"{'Total Investment Value:':<25} ${total_value:,.2f}")

# Optional file saving (to TXT)
save_to_file = input("\nSave portfolio to a file? (y/n): ").lower().strip()
if save_to_file == 'y':
    filename = "portfolio.txt"
    try:
        with open(filename, 'w') as file:
            file.write("Stock Portfolio Summary\n")
            file.write("=" * 40 + "\n\n")
            file.write(f"{'Stock':<8} {'Quantity':<10} {'Value':<12}\n")
            file.write("-" * 30 + "\n")
            for symbol, quantity, value in portfolio:
                file.write(f"{symbol:<8} {quantity:<10} ${value:,.2f}\n")
            file.write("-" * 30 + "\n")
            file.write(f"{'Total:':<25} ${total_value:,.2f}\n")
        print(f"Portfolio saved to {filename}")
    except IOError:
        print("Error saving file. Could not write to disk.")
else:
    print("Portfolio not saved.")
