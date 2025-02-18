# Power calculator using loops in Python without using 'def'

# User input
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Initialize result to 1
result = 1

# Loop to calculate power
for _ in range(exponent):
    result *= base

# Display the result
print(f"The result of {base} raised to the power of {exponent} is {result}")
