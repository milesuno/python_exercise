# Working with loops
total = 0
for price in [15, 12, 8, 26, 93, 18, 8]:
    total += price
    print(f"Running total: {total}")
print(f"Grand Total: £{total}")

# ~~~~~Nested loops~~~~~
# Create coordinates with loops
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")

# Draw F with nested loops
nums = [5, 2, 5, 2, 2]

for num in nums:
    output = ""
    for n in range(num):
        output += "*"
    print(output)

# Find largest Number

numbers =[14, 87, 23, 40, 38, 30, 49]
result = 0

for num in numbers:
    if num >= result:
        result = num
print(result)

# Remove duplicate data
no_doubles = []

for num in nums:
    if num not in no_doubles:
        no_doubles.append(num)

print(no_doubles)

# Tuples are immutable lists (Arrays)
# nums = (1, 2, 3)