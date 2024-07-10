# Prompt the user to enter a number
user_input = int(input("Enter a number: "))

# Initialize the sum variable
total_sum = 0

# Iterate over numbers from 0 to user_input (inclusive)
for i in range(user_input + 1):
    total_sum += i

# Output the result
print(f"The sum of all numbers up to {user_input} is {total_sum}")
