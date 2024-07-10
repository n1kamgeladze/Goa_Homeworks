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