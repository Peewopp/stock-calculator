# Stock Investment Calculator

A simple Python program that calculates the purchase cost, current value,
profit or loss, and percentage return for 10 shares of Apple stock.
The assignment uses fixed example prices: $150 at purchase and $175 afterward.

## Run the program

Requires Python 3. No additional packages are needed.

```sh
python3 investment.py
```

On Windows, use `python investment.py` or `py investment.py`.

Expected output:

```text
Apple Stock Investment
Number of shares: 10
Purchase price per share: $150.00
Investment cost: $1500.00
New price per share: $175.00
Current investment value: $1750.00
Profit or loss: $250.00
Percentage return: 16.67%
```

## Calculations

- Investment cost = number of shares × purchase price per share
- Current investment value = number of shares × new share price
- Profit or loss = current investment value − investment cost
- Percentage return = (profit or loss ÷ investment cost) × 100

## Git versions

The first commit contains Version 1, which calculates the investment cost.
The second commit updates the same `investment.py` file with the investment
value, profit or loss, and percentage return calculations.

View both commits:

```sh
git log --oneline --reverse
```

View Version 1 without changing the current file:

```sh
git show HEAD~1:investment.py
```

Run Version 1 without changing the current file:

```sh
git show HEAD~1:investment.py | python3
```
