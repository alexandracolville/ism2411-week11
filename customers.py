# --- Exercise 1 ---
print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])       # Accessing value using bracket notation
print(customer["email"])      # Accessing value using bracket notation


# --- Exercise 2: Update and add ---
print("--- Exercise 2 ---")
customer["phone"] = "813-555-0142"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# --- Exercise 3 ---
print("--- Exercise 3 ---")

# New Version
print(customer.get("email", "no email on file"))  # Using .get() to safely handle missing keys

# Older version (still used in some codebases)
try:
    print(customer["email"])  # Using bracket notation, which raises an error if missing
except KeyError as error:
    print(f"KeyError Caught: {error}")


# --- Exercise 4 ---
print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)


# --- Exercise 5 ---
print("--- Exercise 5 ---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")       # platinum
print(f"Discount: {discount_rate * 100:.0f}%")  # 15%
print(f"Final price: ${final_price:.2f}")     # $170.00


# --- Exercise 6 ---
print("--- Exercise 6 ---")
# Think of each row in a table/spreadsheet or a record in a database as a dict
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate  # assuming a purchase of $300 for each customer
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")


# --- Exercise 7 ---
print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")


# --- Exercise 8 ---
print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]

print(sales_by_region)
for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")

# Reflection 1: When I would use .get() and when I would use bracket notation:
# You should use bracket notation when you are certain the key exists and want 
# an error raised if it's missing to catch bugs. You should use .get() when 
# a key might occasionally be absent, allowing you to safely handle missing data.

# Reflection 2: What the Exercise 8 summary reminds me of in Excel, and why 
# Python is more useful for large datasets:
# Exercise 8's summary logic is very similar to an Excel Pivot Table or SUMIF formula. 
# Python is more useful for large datasets because it processes millions of rows 
# instantly without becoming sluggish or hitting hard application row limits.