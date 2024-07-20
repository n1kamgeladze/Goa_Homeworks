#1 შექმენთ person ცვლადი dictionary

person = {
    'name': 'nika',
    'age': 19,
    'city': 'Tbilisi',
    'work': 'programming'
    }


print(f"{person['name']} is {person['age']} years old and works as an {person['work']} in {person['city']}.")

#2 შევქმნათ გაკვეთილების ცხრილი და გამოვთვალოს საგნების საშუალო ქულა.
grades = {
    'math': 85,
    'science': 90,
    'history': 78,
    'literature': 92
}

average_grade = sum(grades.values()) / len(grades)

print(f"Math: {grades['math']}")
print(f"Science: {grades['science']}")
print(f"History: {grades['history']}")
print(f"Literature: {grades['literature']}")
print(f"Average grade: {average_grade}")


#3 შევქმნათ საყვარელი წიგნის dictionary
favorite_book = {
    'title': '1984',
    'author': 'George Orwell',
    'year_published': 1949,
    'genre': 'Dystopian, Political Fiction'
}

print(f"My favorite book is '{favorite_book['title']}' by {favorite_book['author']}, published in {favorite_book['year_published']}. It is a {favorite_book['genre']} novel.")

#4 შევქმნათ საშოპინგო ბარათი input და uotput ის გამოყენებით 

# Initialize an empty dictionary for the shopping cart
shopping_cart = {}

# Get the number of items the user wants to buy
num_items = int(input("How many items do you want to buy? "))

# Loop to get item names and their quantities
for i in range(num_items):
    item = input(f"Enter the name of item {i+1}: ")
    quantity = int(input(f"Enter the quantity for {item}: "))
    shopping_cart[item] = quantity

# Print the shopping cart
print("\nYour shopping cart:")
for item, quantity in shopping_cart.items():
    print(f"{item}: {quantity}")