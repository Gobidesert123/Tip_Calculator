print("Welcome to the Tip Calculator")
total_bill = (float(input("What was the total bill? $: ")))
tip = (int(input("How much tip would you like to give?, 10, 12, 15?")))
split_between = (int(input("How many people would split the bill?")))
total = (total_bill * (tip/100) + total_bill)/split_between
r_total = round(total, 2)
print(f"Each person should pay: $ {r_total}")
print("new change")
