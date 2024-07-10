#1 Remove and print the last element of a list of integers:

def pop_last_element(int_list):
    if int_list:
        return int_list.pop()
    else:
        return None

# Example usage
numbers = [1, 2, 3, 4, 5]
print(pop_last_element(numbers))  # Output: 5
print(numbers)  # Output: [1, 2, 3, 4]
 
#Remove and return the first element of a list of strings:

def pop_first_element(str_list):
    if str_list:
        return str_list.pop(0)
    else:
        return None

# Example usage
words = ["apple", "banana", "cherry"]
print(pop_first_element(words))  # Output: "apple"
print(words)  # Output: ["banana", "cherry"]








