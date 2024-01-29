
#Task_N1
'''
1.დაწერე პროგრამა რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.
'''
print("Task_N1")

mul_by = lambda a, lst: [x * a for x in lst]
my_list = [1, 2, 3, 4, 5]
y = 137.5

result = mul_by(y, my_list)
print(f"Result is: {result}")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print()


#task_N2
'''
2.დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს,
მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება.  (გამოიყენე .isupper() მეთოდი)
'''
print("task_N2")

length_Final = lambda n_list: len(list(filter(lambda name: name[0].isupper(), n_list)))

names = ['David', 'dato', 'Sopho', 'mari', 'Niko', 'Jimicu']
names2 = ['Tbilisi','baku','Erevan', 'istanbul','doneckebi',"Kharkovebi"]

result = length_Final(names)

print(f"Result is: {result}")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print()

#task_N3
'''
3.	დაწერე პროგრამა რომელიც დააჯამებს სიაში არსებულ დადებით და უარყოფით რიცხვებს ცალცალკე. გამოიყენე ლამბდა ფუნქცია და filter.
'''

print("task_N3")

import random
sum_P_N = lambda num_list: (
    sum(filter(lambda x: x > 0, num_list)),
    sum(filter(lambda x: x < 0, num_list))
)

ran_num = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
ran_num2 = [random.randint(-10, 10) for i in range(10)]

print("Random Numbers:", ran_num2)

P_sum, N_sum = sum_P_N(ran_num2)


print("Sum of positive numbers is:", P_sum)
print("Sum of negative numbers is:", N_sum)

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print()

#Task_N4

''' 
4.	დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების და შემდგომ ექაუნთში შესვლის პროგრამა,
არასწორი ინფორმაციის შეყვანა მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით.
'''
print("Task_N4")

def create_account():
    account_number = input("Enter acc number: ")
    pin = input("Create a PIN: ")
    balance = 0
    return account_number, pin, balance

def deposit_money(balance, amount):
    balance = balance + amount
    print(f"Deposit successful. Current balance is : {balance} GEL ")
    return balance

def login(account_info, entered_account_number, entered_pin):
    try:
        account_number, pin, balance = account_info
        if entered_account_number == account_number and entered_pin == pin:
            print("Login successful.")
            print(f"Account Number: {account_number}")
            print(f"Balance: {balance} GEL")
        else:
            raise ValueError("Invalid account number or PIN. Please try again.")
    except ValueError as e:
        print(f"Error: {e}")

try:
    account_info = create_account()

    deposit_amount = float(input("Enter deposit amount: GEL "))
    account_info = (account_info[0], account_info[1], deposit_money(account_info[2], deposit_amount))

    entered_account_number = input("Enter account number for login: ")
    entered_pin = input("Enter PIN for login: ")

    login(account_info, entered_account_number, entered_pin)

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
print()
