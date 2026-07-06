"""
Stock Portfolio Tracker
A simple tracker that calculates total investment value based on
manually defined (hardcoded) stock prices.
"""

import csv
from datetime import datetime

# Hardcoded stock prices (price per share, in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 175,
    "MSFT": 420,
    "NFLX": 650,
}


def show_available_stocks():
    """Display the list of stocks and their prices."""
    print("\nAvailable stocks:")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price:>8.2f}")
    print("-" * 30)


def get_portfolio_input():
    """
    Prompt the user to enter stock symbols and quantities.
    Returns a list of dicts: [{"symbol": "AAPL", "quantity": 10, "price": 180, "value": 1800}, ...]
    """
    portfolio = []

    print("\nEnter your stock holdings one at a time.")
    print("Type 'done' as the stock name when you're finished.\n")

    while True:
        symbol = input("Stock symbol (or 'done' to finish): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the price list. Please choose from the available stocks.")
            continue

        quantity_input = input(f"Quantity of {symbol}: ").strip()

        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("Please enter a valid positive whole number for quantity.")
            continue

        quantity = int(quantity_input)
        price = STOCK_PRICES[symbol]
        value = price * quantity

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": value,
        })

        print(f"Added: {quantity} share(s) of {symbol} @ ${price:.2f} = ${value:.2f}\n")

    return portfolio


def display_summary(portfolio):
    """Print a formatted summary of the portfolio and total investment."""
    if not portfolio:
        print("\nNo stocks were added. Nothing to summarize.")
        return 0

    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Symbol':<10}{'Qty':<8}{'Price':<12}{'Value':<12}")
    print("-" * 45)

    total_investment = 0
    for holding in portfolio:
        print(f"{holding['symbol']:<10}{holding['quantity']:<8}"
              f"${holding['price']:<11.2f}${holding['value']:<11.2f}")
        total_investment += holding["value"]

    print("-" * 45)
    print(f"{'TOTAL INVESTMENT:':<30}${total_investment:.2f}")
    print("=" * 45)

    return total_investment


def save_to_file(portfolio, total_investment):
    """Optionally save the portfolio summary to a .txt or .csv file."""
    choice = input("\nWould you like to save this summary to a file? (y/n): ").lower().strip()

    if choice != "y":
        print("Summary not saved.")
        return

    file_format = input("Choose format - txt or csv: ").lower().strip()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if file_format == "csv":
        filename = f"portfolio_summary_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for holding in portfolio:
                writer.writerow([holding["symbol"], holding["quantity"],
                                  holding["price"], holding["value"]])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_investment])
        print(f"Summary saved to {filename}")

    elif file_format == "txt":
        filename = f"portfolio_summary_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            f.write(f"{'Symbol':<10}{'Qty':<8}{'Price':<12}{'Value':<12}\n")
            f.write("-" * 45 + "\n")
            for holding in portfolio:
                f.write(f"{holding['symbol']:<10}{holding['quantity']:<8}"
                         f"${holding['price']:<11.2f}${holding['value']:<11.2f}\n")
            f.write("-" * 45 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total_investment:.2f}\n")
        print(f"Summary saved to {filename}")

    else:
        print("Unrecognized format. Summary not saved.")


def main():
    print("=" * 45)
    print("STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    show_available_stocks()
    portfolio = get_portfolio_input()
    total_investment = display_summary(portfolio)

    if portfolio:
        save_to_file(portfolio, total_investment)

    print("\nThanks for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
