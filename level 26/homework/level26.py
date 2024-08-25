def transform_list(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:  # Even number
            new_list.append(num // 2)
        else:  # Odd number
            new_list.append(num * 2)
    return new_list

# Test cases
print(transform_list([1, 2, 3, 4]))  # Output: [2, 1, 6, 2]
print(transform_list([5, 10, 3, 5]))  # Output: [10, 5, 6, 10]