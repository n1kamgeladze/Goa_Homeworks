#Len Tasks

#1 Find the length of a list of 10 random integers:
import random

def length_of_random_integers():
    random_integers = [random.randint(1, 100) for _ in range(10)]
    return len(random_integers)

# Example usage
print(length_of_random_integers())  # Output: 10

#2 Determine the number of elements in a list of strings representing weekdays:
def number_of_weekdays(weekdays_list):
    return len(weekdays_list)

# Example usage
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(number_of_weekdays(weekdays))  # Output: 7

#3 Calculate the length of a nested list:
def length_of_nested_list(nested_list):
    return len(nested_list)

# Example usage
nested = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(length_of_nested_list(nested))  # Output: 4