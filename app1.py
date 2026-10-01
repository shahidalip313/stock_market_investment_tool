# STOCK MARKET INVESTMENT TOOL

def percentage_to_cash(investable_amount, asset_percentage):
    '''Convert percentge asset allocation to cash value'''
    asset_investable = investable_amount * asset_percentage / 100
    rounded_asset_investable = round(asset_investable, 2)
    return rounded_asset_investable


def get_allocation(age):
    '''Function to return equity, large_cap, mid_cap, small_cap, debt, gold'''
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

    return equity, large_cap, mid_cap, small_cap, debt, gold

def main():
    print("Welcome to stock market investment tool")
    age = int(input("Enter your age:"))
    salary = int(input("Enter your salary: "))
    expense = int(input("Enter you expense: "))

    investable_amount = salary - expense
    print("Investable amount is:", investable_amount)
    equity, large_cap, mid_cap, small_cap, debt, gold = get_allocation(age)

    print("Reccomended Asset Allocation: ")
    print("Equity : ₹ ", percentage_to_cash(investable_amount, equity))
    print("    Large cap : ₹ ", percentage_to_cash(investable_amount, large_cap))
    print("    Mid cap : ₹ ", percentage_to_cash(investable_amount, mid_cap))
    print("    Small cap : ₹ ", percentage_to_cash(investable_amount, small_cap))
    print("    Debt : ₹ ", percentage_to_cash(investable_amount, debt))
    print("Gold / Alternatives : ₹ ", percentage_to_cash(investable_amount, gold))
if __name__=="__main__":
    main()