#Min Tasks

#1 Find the smallest number in a list of integers:
def min_number(int_list):
    return min(int_list) if int_list else None

# Example usage
numbers = [4, 1, 7, 3, 2]
print(min_number(numbers))  # Output: 1

#Find the shortest word in a list of strings:
def shortest_word(str_list):
    return min(str_list, key=len) if str_list else None

# Example usage
words = ["apple", "banana", "cherry", "fig"]
print(shortest_word(words))  # Output: "fig"

#Find the lowest temperature in a list of daily temperatures:
def lowest_temperature(temp_list):
    return min(temp_list) if temp_list else None

# Example usage
temperatures = [72, 68, 75, 70, 65]
print(lowest_temperature(temperatures))  # Output: 65

#Find the minimum price in a list of products:
def min_price(product_list):
    return min(product_list) if product_list else None

# Example usage
prices = [19.99, 24.99, 4.99, 29.99]
print(min_price(prices))  # Output: 4.99