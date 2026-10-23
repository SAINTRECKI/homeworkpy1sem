import re

products = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]

pattern = r"PRD-\d{5}"

valid_products = []

for product in products:
    if re.fullmatch(pattern, product):
        valid_products.append(product)

print(valid_products)