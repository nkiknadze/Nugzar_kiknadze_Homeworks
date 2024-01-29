#Task_N1
'''
1.დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს "ტექსტურ ფაილში"
ინფორმაციას Input ფუნქციის დახმარებით, მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.
'''
print("Task_N1")



def write_to_file():
    with open("Task_13.txt", "w") as file:
        while True:
            input1 = input("Enter the information or enter 'enough' to stop): ")
            if input1.lower() == 'enough':
                break
            file.write(input1 + '\n')

write_to_file()
print()

#Task_N2
'''
2.დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და 
შესაქმნელი ფაილის სახელს,
შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში არსებულ ყველა ფაილის სიას.
#დაშვებას ვაკეთებთ რომ მომხმარებელს სწორად შეჰყავს ლოკაცია და ფაილის დასახელება. ეს დავამატე პირობაში
'''
print("Task_N2")
import os

def fun1():
    location = input("Enter the folder location: ")
    file_name = input("Enter the file name: ")

    file_path = location + '/' + file_name + '.txt'
    
    with open(file_path, 'w') as file:
        file.write("martivi texturi faili. ")

    file_list = os.listdir(location)

    print(f"Files are: {location}:")
    for file in file_list:
        print(file)

fun1()
print()
