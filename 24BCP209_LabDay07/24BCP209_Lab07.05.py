# 05. Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.

def create_dict(key_prompt, value_prompt):
    user_dict = {}

    for i in range(num_entries):
        key = input(f"Enter {key_prompt} {i + 1}: ")
        value = int(input(f"Enter {value_prompt} of {key}: "))
        user_dict[key] = value

    return user_dict 

def count_TotalBill():
    total_bill = 0

    for item, quantity in grocery_quantities.items():
        if item in grocery_prices:
            total_bill += grocery_prices[item] * quantity
        else:
            print(f"Warning: '{item}' not found in the price dictionary.")

    return total_bill

num_entries = int(input("Enter No. of Grocery items which you want to buy : "))
print("\nDictionary of Grocery items along with their price :-")
grocery_prices = create_dict("Grocery item","Price")
print("\nDictionary of Grocery items along with their quantity :-")
grocery_quantities = create_dict("Grocery item","Quantity")

print(f"\n{grocery_prices}")
print(grocery_quantities)
print("\nTotal bill: ₹", count_TotalBill())