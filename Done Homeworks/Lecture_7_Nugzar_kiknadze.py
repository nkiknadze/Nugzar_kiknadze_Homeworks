

#task_N1

'''
1.	რეკურსიის დახმარებით შექმენი ფუნქცია, რომელიც იმდენჯერ დაბეჭდავს მისალმებას, რა რიცხვსაც გადასცემ არგუმენტად. (ციკლის გამოყენება არ შეიძლება)
'''
print("Task_N1")

def greeting(n):
    if n > 0:
        print("Hello!")
        greeting(n - 1)

num = int(input("Enter the Num: "))
greeting(num)
print()

#task_N2
'''
2.	შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და რაოდენობას და დაბეჭდავს მას, თუმცა რაოდენობას თუ არ მივუთითებთ შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.
'''

print("Task_N2")

def order(dish_name, quantity_input=""):
    if quantity_input.strip() == "":
        quantity = 1
    else:
        quantity = int(quantity_input)
    print(f"Order is: {quantity} {dish_name}")

dish_name = input("Enter the Dish Name: ")
quantity_input = input("Enter the quantity: ")

order(dish_name, quantity_input)
print()

#task_N3
'''
3.	შექმენი ფუნქცია, რომელიც მიიღებს მინიმუმ 3 რიცხვს,  და დააბრუნებს და დაბეჭდავს ნამრავლს.
'''
print("task_N3")

def multiply_of_numbers(*args):
    product = 1
    for num in args:
        product *= num
    return product

numbers = []

while True:
    user_input = input("Enter a numb (or 'END' to stop): ")        
    if user_input.upper() == 'END':
        if len(numbers) >= 3:
            break
        else:
            print("Error: Minimum 3 num are required. Process stopped.")
            break
    elif user_input.replace(".", "", 1).isdigit() or (user_input[0] == '-' and user_input[1:].replace(".", "", 1).isdigit()):
        num = float(user_input)
        numbers.append(num)
    else:
        print("Invalid input. Please enter a num!")
if len(numbers) >= 3:
    result = multiply_of_numbers(*numbers)
    print(f"The multiply of the numbers is: {result}")
print()
