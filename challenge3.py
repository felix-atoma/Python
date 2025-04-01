
# Function to check if base^exponent is greater than 5000
def large_power(base, exponent):
    result = base ** exponent
    return result > 5000

# Function to check if a number is divisible by 10
def divisible_by_ten(num):
    return num % 10 == 0

# Example usage
print(large_power(10, 3))  # True (1000 is less than 5000)
print(large_power(5, 5))   # True (3125 is less than 5000)
print(divisible_by_ten(20)) # True
print(divisible_by_ten(33)) # False
