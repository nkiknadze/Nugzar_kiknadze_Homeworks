
#task_N2

print("Task_N2 'Multiplication Table' ")

n = int(input("Enter_num: "))

if n <= 0:
    print("Please enter a positive integer.")

print(f"Multiplication Table up to {n}:")

for i in range(1, n + 1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

print()


#Task_N3

print("Task_N3 'Account Balance' ")

balance = 3000

while True:
        cost = float(input("Enter the cost (enter 0 to stop): "))

        if cost == 0:
            break

        if cost > balance:
            print("Not enough money!")
        else:
            balance -= cost
            print(f"Amount remaining in the account: {balance} GEL\n")

print(f"Final amount in the account is: {balance} GEL")

print()


#Task_N4

print("Task_N4 'Parrot' ")

while True:
    question = input("say a word or (quit) to exit: ")

    if question.lower().strip() == 'quit':
        print("Goodbye!")
        break

    print("User Said Whaaat!?")
    print(f"User Said {question}\n")
