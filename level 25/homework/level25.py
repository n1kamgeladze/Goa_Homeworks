def transform_list(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:  # თუ რიცხვი ლუწია
            new_list.append(num / 2)
        else:  # თუ რიცხვი კენტია
            new_list.append(num * 2)
    return new_list

# მაგალითები
print(transform_list([1, 2, 3, 4]))  # -> [2, 1, 6, 2]
print(transform_list([5, 10, 3, 5])) # -> [10, 5, 6, 10]