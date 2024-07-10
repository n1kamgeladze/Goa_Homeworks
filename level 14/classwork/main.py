#Max Tasks
#1 Find the maximum number in a list of integers:
def max_number(int_list):
    return max(int_list) if int_list else None

# Example usage
numbers = [1, 2, 3, 4, 5]
print(max_number(numbers))  # Output: 5

#2 Find the maximum string length in a list of strings:
def max_string_length(str_list):
    return max(len(s) for s in str_list) if str_list else None

# Example usage
words = ["apple", "banana", "cherry"]
print(max_string_length(words))  # Output: 6

#3 Find the oldest person's age in a list of ages:
def oldest_age(age_list):
    return max(age_list) if age_list else None

# Example usage
ages = [25, 30, 45, 50, 20]
print(oldest_age(ages))  # Output: 50

#4 Find the most recent date in a list of datetime objects:
from datetime import datetime

def most_recent_date(date_list):
    return max(date_list) if date_list else None

# Example usage
dates = [datetime(2023, 5, 17), datetime(2023, 6, 17), datetime(2023, 7, 17)]
print(most_recent_date(dates))  # Output: 2023-07-17 00:00:00


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