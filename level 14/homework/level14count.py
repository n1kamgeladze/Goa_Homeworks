#Count Tasks
#1 Count how many times the number 5 appears in a list of integers:

def count_fives(int_list):
    return int_list.count(5)

# Example usage
numbers = [5, 1, 5, 2, 5, 3]
print(count_fives(numbers))  # Output: 3

#2 Count occurrences of the letter 'a' in a list of strings:
def count_a(str_list):
    return sum(s.count('a') for s in str_list)

# Example usage
words = ["apple", "banana", "cherry"]
print(count_a(words))  # Output: 4

#3 Count the number of True values in a list of boolean values:
def count_true(bool_list):
    return bool_list.count(True)

# Example usage
bools = [True, False, True, True]
print(count_true(bools))  # Output: 3

#4 Count occurrences of a sublist [3, 4] in a nested list:
def count_sublist(nested_list, sublist):
    return sum(1 for i in range(len(nested_list) - len(sublist) + 1) if nested_list[i:i + len(sublist)] == sublist)

# Example usage
nested = [[1, 2], [3, 4], [5, 6], [3, 4]]
print(count_sublist(nested, [3, 4]))  # Output: 2