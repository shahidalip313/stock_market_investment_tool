# OVERALL SUMMARY
# 1. Create a tkinter app
# 2. Fetch age from user
# 3. Fetch salary from user
# 4. Fetch expense from user
# 5. Button to calculate investable amount
# 6. DDisplay asset alocation based on age and investable amount

from app1 import percentage_to_cash, get_allocation

def calculate_allocation():
    age = int(age_entry.get())
    salary = float(salary_entry.get())
    expense = float(expense_entry.get())

    investable_amount = salary - expense 

    equity, large_cap, mid_cap, small_cap, debt, gold = get_allocation(age)

    result = f"""Investable amount:₹{investable_amount}

Investment Breakdown:
Equity: ₹{percentage_to_cash(investable_amount, equity)}
Large Cap: ₹{percentage_to_cash(investable_amount, large_cap)}
Mid Cap: ₹{percentage_to_cash(investable_amount, mid_cap)}
Small Cap: ₹{percentage_to_cash(investable_amount, small_cap)}
Debt: ₹{percentage_to_cash(investable_amount, debt)}
Gold / Alternatives: ₹{percentage_to_cash(investable_amount, gold)}"""

    result_label.config(text=result)


# 1. Create a tkinter app
import tkinter as tk

root = tk.Tk()
root.title("Stock Market Investment Tool")
root.geometry("500x450")

label = tk.Label(root, text="Enter your details", font=("Arial", 14, "bold"))
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# 2. Fetch age from user
age_label = tk.Label(frame, text="Age:")
age_label.grid(row=0, column=0, pady=5, sticky="w")

age_entry = tk.Entry(frame)
age_entry.grid(row=0, column=1, pady=5, sticky="w")

# 3. Fetch salary from user
salary_label = tk.Label(frame, text="Monthly Salary:")
salary_label.grid(row=1, column=0, pady=5, sticky="w")

salary_entry = tk.Entry(frame)
salary_entry.grid(row=1, column=1, pady=5)

# 4. Fetch expense from user
expense_label = tk.Label(frame, text="Monthly expenses:")
expense_label.grid(row=2, column=0, pady=5)

expense_entry = tk.Entry(frame)
expense_entry.grid(row=2, column=1, pady=5)

# 5. Button to calculate investable amount
button = tk.Button(root, text="Calculate investment", command=calculate_allocation)
button.pack(pady=15)

# 6. DDisplay asset alocation based on age and investable amount
result_label = tk.Label(root, text="", justify="left", font=("Corier New", 10))
result_label.pack()


root.mainloop()