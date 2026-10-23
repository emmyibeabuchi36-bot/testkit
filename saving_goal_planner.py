# Saving Goal Planner

# 1. Get the user's savings goal
goal = float(input("Enter your savings goal: "))

total_yearly_savings = 0

# 2–5. Enter savings sources in a loop
while True:
    source = input("\nEnter the name of your savings source: ")
    amount = float(input(f"Enter the amount saved from {source}: "))
    times_per_year = int(input(f"How many times do you make this saving in a year? "))

    # Calculate the yearly contribution from this source
    yearly_saving = amount * times_per_year
    total_yearly_savings += yearly_saving

    print(f"Yearly saving from {source}: {yearly_saving:,.2f}")

    # Ask if the user wants to add another source
    another = input("\nDo you want to add another savings source? (yes/no): ").lower()

    if another != "yes":
        break

# 6. Calculate the number of years required
if total_yearly_savings > 0:
    years = goal / total_yearly_savings

    # Round up to the next whole year
    years = int(years) if years == int(years) else int(years) + 1

    print("\n--- Saving Goal Summary ---")
    print(f"Savings goal: {goal:,.2f}")
    print(f"Total yearly savings: {total_yearly_savings:,.2f}")
    print(f"Estimated time to reach goal: {years} year(s)")
else:
    print("\nYou have not entered any savings.")
