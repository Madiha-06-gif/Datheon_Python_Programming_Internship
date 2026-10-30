
import csv
def load_valid_tickers():
    valid_tickers = set()

    with open("constituents.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            valid_tickers.add(row["Symbol"].strip().upper())

    return valid_tickers


valid_tickers = load_valid_tickers()

portfolio = {}

print("INVESTMENT PORTFOLIO TRACKER")
print("-" * 35)

while True:
    ticker = input("\nEnter stock ticker (e.g., AAPL): ").strip().upper()

    if not ticker:
        print("Ticker cannot be empty.")
        continue
    if ticker not in valid_tickers:
        print("Invalid ticker. Please enter an S&P 500 company symbol.")
        continue

    if ticker in portfolio:
        print("This stock is already added. Enter a different ticker.")
        continue

    try:
        buy_price = float(input("Enter buy price: "))
        quantity = int(input("Enter number of shares: "))
        current_price = float(input("Enter current price: "))

        if buy_price <= 0 or current_price <= 0 or quantity <= 0:
            print("Prices and quantity must be greater than zero.")
            continue

    except ValueError:
        print("Invalid input. Enter valid numbers.")
        continue

    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": current_price
    }

    another = input("Add another stock? (yes/no): ").strip().lower()

    if another != "yes":
        break

total_invested = 0
total_current_value = 0

with open("portfolio_summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Ticker", "Buy Price", "Quantity", "Current Price",
        "Invested Amount", "Current Value", "Profit/Loss", "Gain/Loss (%)"
    ])

    for ticker, details in portfolio.items():
        invested = details["buy_price"] * details["quantity"]
        current_value = details["current_price"] * details["quantity"]
        profit_loss = current_value - invested
        percentage = (profit_loss / invested) * 100

        total_invested += invested
        total_current_value += current_value

        print(f"\nStock: {ticker}")
        print(f"Invested: ${invested:.2f}")
        print(f"Current value: ${current_value:.2f}")
        print(f"Profit/Loss: ${profit_loss:.2f}")
        print(f"Gain/Loss: {percentage:.2f}%")

        writer.writerow([
            ticker, details["buy_price"], details["quantity"],
            details["current_price"], round(invested, 2),
            round(current_value, 2), round(profit_loss, 2),
            round(percentage, 2)
        ])

total_profit_loss = total_current_value - total_invested

if total_invested > 0:
    total_percentage = (total_profit_loss / total_invested) * 100
else:
    total_percentage = 0

print("\n" + "-" * 35)
print("PORTFOLIO SUMMARY")
print(f"Total invested: ${total_invested:.2f}")
print(f"Total current value: ${total_current_value:.2f}")
print(f"Total profit/loss: ${total_profit_loss:.2f}")
print(f"Overall gain/loss: {total_percentage:.2f}%")

print("\nResults saved to portfolio_summary.csv")
