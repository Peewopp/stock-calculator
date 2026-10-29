# Calculate the cost of buying 10 shares of Apple stock.
number_of_shares = 10
share_price = 150

investment_cost = number_of_shares * share_price

print("Apple Stock Investment")
print(f"Number of shares: {number_of_shares}")
print(f"Purchase price per share: ${share_price:.2f}")
print(f"Investment cost: ${investment_cost:.2f}")

# Calculate the investment value, profit or loss, and percentage return.
new_share_price = 175

current_investment_value = number_of_shares * new_share_price
profit_or_loss = current_investment_value - investment_cost
percentage_return = (profit_or_loss / investment_cost) * 100

print(f"New price per share: ${new_share_price:.2f}")
print(f"Current investment value: ${current_investment_value:.2f}")
print(f"Profit or loss: ${profit_or_loss:.2f}")
print(f"Percentage return: {percentage_return:.2f}%")
