#მოვითხოვოთ ინტეჯერი(ციფრი/რიცხვი)
a = int(input("enter the first number: "))
#მოვითხოვოთ მოქმედება 
choice = input("enter your choice: ")
#მოვითხოვოთ მეორე ინტეჯერი
b = int(input("enter the second number: "))

#გამოვიყენოტ if, elif, else მოქმედებების შედეგების მისაღებად
if choice == '+':
    print(a + b)
elif choice == "-" :
    print(a - b)
elif choice == "*" :
    print(a * b)
elif choice == '/':
    print(a / b)
#სხვა შემთხვევაში დავპრინტოთ შეცდომა
else: 
    print("error")