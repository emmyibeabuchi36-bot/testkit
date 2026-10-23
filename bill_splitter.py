# PROJECT: BILL SPLITTER

# 1. Get the total bill amount
bill = float(input("Enter the total bill amount: "))

# 2. Get the split ratio
print("\nEnter the split ratio (e.g. 1:3:5:4).")
print("WARNING: Do not add spaces around the colons.")

ratio = input("Enter split ratio: ")

# 3. Parse the split ratio using string methods
parts = ratio.split(":")

# Convert each part of the ratio from string to integer
values = [int(part) for part in parts]

# Calculate the total of all ratio values
total_ratio = sum(values)

# 4. Split the bill according to the ratio
print("\n--- BILL SPLIT ---")

# 5. Print how much each member should pay
for i, value in enumerate(values, start=1):
    amount_to_pay = (value / total_ratio) * bill
    print(f"Member {i} pays: {amount_to_pay:.2f}")
