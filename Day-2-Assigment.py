print("Welcome to the ti calculator")
bill_amount = float(input("enter the total bill amount"))
tip_amount = int(input("How much tip would you like to give?: 10 or 12 or 15?"))
split_person = int(input("How many people to split the bill"))
amount = (bill_amount * tip_amount)/100

split_amount =(bill_amount + amount) / split_person

print(f"Each person should pay $:{split_amount}")