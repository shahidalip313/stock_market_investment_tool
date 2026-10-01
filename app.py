# STOCK MARKET INVESTMENT TOOL

print("Welcome to stock market investment tool")

age = int(input("Enter your age:"))

# Conditions 
if age <= 20:
    equity = 90; large_cap = 50; mid_cap = 25; small_cap = 15; debt = 5; gold = 5
elif age <= 30:
    equity = 80; large_cap = 50; mid_cap = 20; small_cap = 10; debt = 15; gold = 5
elif age <= 40:
    equity = 70; large_cap = 45; mid_cap = 15; small_cap = 10; debt = 20; gold = 10
elif age <= 50:
    equity = 60; large_cap = 40; mid_cap = 15; small_cap = 5; debt = 30; gold = 10
elif age <= 60:
    equity = 50; large_cap = 35; mid_cap = 10; small_cap = 5; debt = 40; gold = 10
else:
    equity = 30; large_cap = 25; mid_cap = 25; small_cap = 0; debt = 60; gold = 10

print("Reccomended Asset Allocation: ")
print("Equity : ", equity, "%")
print("    Large cap : ", large_cap, "%")
print("    Mid cap : ", mid_cap, "%")
print("    Small cap : ", small_cap, "%")
print("    Debt : ", debt, "%")
print("Gold / Alternatives : ", gold, "%")