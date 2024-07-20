#1 იპოვეთ ლისტში ყველაზე პატარა წევრი min ფუნქციის გამოყენების გარეშე.
def find_min(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest

my_list = [5, 3, 8, 1, 2]
print(find_min(my_list))


#2 იპოვეთ ლისტში ყველაზე დიდი წევრი max ფუნქციის გამოყენების გარეშე.
def find_max(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

my_list = [5, 3, 8, 1, 2]
print(find_max(my_list))


#3 გამოიტანეთ 1, 3 და 5 წევრების ინდექსები.
my_list = [10, 20, 30, 40, 50, 60]
indices = [1, 3, 5]
selected_elements = [my_list[i] for i in indices]
print(selected_elements)


#4 გააერთიანეთ ორი ლისტი ისე რომ ყოველი ინტეჯერის შემდეგ მოდიოდეს სტრინგი.
integers = [1, 2, 3]
strings = ["a", "b", "c"]
combined_list = []

for i in range(max(len(integers), len(strings))):
    if i < len(integers):
        combined_list.append(integers[i])
    if i < len(strings):
        combined_list.append(strings[i])

print(combined_list)


#5 ამოიღეთ ლისტიდან ინტეჯერები და სტრინგები და განათავსეთ ისინი ცალკე სიებში.
mixed_list = [1, "a", 2, "b", 3, "c"]
integers = []
strings = []

for item in mixed_list:
    if isinstance(item, int):
        integers.append(item)
    elif isinstance(item, str):
        strings.append(item)

print(integers)
print(strings)


#6 ამოიღეთ კენტები და ლუწები და დაპრინტოთ მათი ჯამი ცალ-ცალკე.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [10, 11, 12]

all_lists = list1 + list2 + list3 + list4
even_sum = 0
odd_sum = 0

for num in all_lists:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")


#7 ამოიღეთ კენტები და ლუწები და განათავსეთ ორ სხვადასხვა სიაში.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
list4 = [10, 11, 12]

all_lists = list1 + list2 + list3 + list4
even_numbers = []
odd_numbers = []

for num in all_lists:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(even_numbers)
print(odd_numbers)


#8 სტრინგების სიგრძეების შეყვანა მეორე სიაში.
strings = ["apple", "banana", "cherry"]
lengths = [len(s) for s in strings]
print(lengths)


#9 ყველა ინტეჯერის შეკრება და სტრინგების შეერთება.
mixed_lists = [
    [1, "a", 2],
    ["b", 3, "c"],
    [4, "d"]
]

total_sum = 0
combined_string = ""

for lst in mixed_lists:
    for item in lst:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, str):
            combined_string += item

print(f"Sum of all integers: {total_sum}")
print(f"Combined string: {combined_string}")


#10 ლუწ ინდექსზე მყოფი ელემენტების გადატანა ახალ სიაში.
my_list = [10, 20, 30, 40, 50, 60]
even_index_elements = [my_list[i] for i in range(len(my_list)) if i % 2 == 0]
print(even_index_elements)