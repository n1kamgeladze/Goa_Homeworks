#Sum Tasks

#1 Calculate the sum of all numbers in a list of integers:
def sum_numbers(int_list):
    return sum(int_list)

# Example usage
numbers = [1, 2, 3, 4, 5]
print(sum_numbers(numbers))  # Output: 15

#2 Calculate the total length of strings in a list of strings:
def total_length(str_list):
    return sum(len(s) for s in str_list)

# Example usage
words = ["apple", "banana", "cherry"]
print(total_length(words))  # Output: 17

#3 Calculate the total score of a team in a list of game results:
def total_score(scores_list):
    return sum(scores_list)

# Example usage
scores = [10, 15, 20, 25]
print(total_score(scores))  # Output: 70

#4 Sum the elements of nested lists to get a flattened sum:
def sum_nested_lists(nested_list):
    return sum(sum(inner_list) for inner_list in nested_list)

# Example usage
nested = [[1, 2], [3, 4], [5, 6]]
print(sum_nested_lists(nested))  # Output: 21