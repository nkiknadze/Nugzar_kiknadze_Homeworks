# _ _ _ _ _ _ _ _ _ _ _ _ _ _
# Task_N1
# _ _ _ _ _ _ _ _ _ _ _ _ _ _

print("Task_N1")

info = []
count = 3

for i in range(count):
    name = input(f"Enter name for user {i + 1}: ")
    surname = input(f"Enter surname for user {i + 1}: ")
    age = input(f"Enter age for user {i + 1}: ")

    user_info = [name, surname, age]
    info.append(user_info)

while True:
    user_index = int(input("Please choose the Number: "))

    if 0 <= user_index and user_index < len(info):
        selected_user = info[user_index]
        print("Name: {}".format(selected_user[0]))
        print("Lastname: {}".format(selected_user[1]))
        print("Age: {}".format(selected_user[2]))
        break
    else:
        print("Invalid user index. Please enter a valid index.")

print()

# _ _ _ _ _ _ _ _ _ _ _ _ _ _
# Task_N2
# _ _ _ _ _ _ _ _ _ _ _ _ _ _

print("Task_N2")

data = []

name = input("Enter your Name: ")
password = input("Enter your password (at least 8 characters) for registration: ")

while True:
    if name != "" and len(password) >= 8:
        data.append([name, password])
        print("Registration successful!")
        break
    else:
        print("Invalid registration. Name cannot be empty or/and password must be at least 8 characters.")
    break


login_name = input("Enter your name for login: ")
login_password = input("Enter your password for login: ")

if [login_name, login_password] in data:
    print("Login successful!")
else:
    print("Login failed. Incorrect name or password.")
print()

# # _ _ _ _ _ _ _ _ _ _ _ _ _ _
# # Task_N3
# # _ _ _ _ _ _ _ _ _ _ _ _ _ _

print("Task_N3")

actors_info = [
    {"first_name": "Kakhi", "last_name": "Kavsadze", "age": "Dead", "nationality": "Georgian"},
    {"first_name": "Iron Man", "last_name": "Tony Stark", "age": 45, "nationality": "American"},
    {"first_name": "Adriano", "last_name": "Celentano", "age": 85, "nationality": "Italian"}]


search_name = input("Enter actor's first or last name: ").strip()

actor_found = False
for actor in actors_info:
    if search_name.lower().strip() in (actor["first_name"] + actor["last_name"]).lower().strip():
        print(f" Actor found!\n Name: {actor['first_name']}\n Surname: {actor['last_name']}\n Age: {actor['age']}\n Nationality: {actor['nationality']}")
        actor_found = True
        break
if not actor_found:
    print("Actor not found in the list.")
print()