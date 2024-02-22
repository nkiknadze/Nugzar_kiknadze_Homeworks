
#TASK N1
print ("TASK_N1")

a = "1. Sumerians"
b = "2. Seljuks"
c = "3. Rome"
d = "4. Mongols"

question = (f"Which empire's water supply system (aqueduct) is still functioning today?\n\
{a}\n\
{b}\n\
{c}\n\
{d}\n")

correct_answer = '3'

ask = input (question)

if ask == correct_answer or ask.lower().strip() == 'rome':
    print ('Correct!')
else:
    print ('No! The correct answer is Rome!')


# Task N2
print("Task_N2")

Prod1 = 'notebook'
Prod2 = 'pc'
Prod3 = 'mobile'

notebook1 = 'lenovo'
notebook2 = 'hp'
notebook3 = 'asus'

PC1 = 'lenovo'
PC2 = 'hp'
PC3 = 'asus'

mob1 = 'samsung'
mob2 = 'apple'
mob3 = 'nokia'

price1 = 500
price2 = 1000
price3 = 1500

question1 = input(f"What product do you want to buy, {Prod1}, {Prod2}, or {Prod3}? ").lower().strip()

if question1 == Prod1 or question1 == Prod2 or question1 == Prod3:
    question2 = float(input("Please enter your budget: "))
    
    if question1 == Prod1 and question2 >= price3:
        print(f"{Prod1}_{notebook3}_{price3}$")
    elif question1 == Prod1 and question2 >= price2:
        print(f"{Prod1}_{notebook2}_{price2}$")
    elif question1 == Prod1 and question2 >= price1:
        print(f"{Prod1}_{notebook1}_{price1}$")
    elif question1 == Prod2 and question2 >= price3:
        print(f"{Prod2}_{PC3}_{price3}$")
    elif question1 == Prod2 and question2 >= price2:
        print(f"{Prod2}_{PC2}_{price2}$")
    elif question1 == Prod2 and question2 >= price1:
        print(f"{Prod2}_{PC1}_{price1}$")
    elif question1 == Prod3 and question2 >= price3:
        print(f"{Prod3}_{mob3}_{price3}$")
    elif question1 == Prod3 and question2 >= price2:
        print(f"{Prod3}_{mob2}_{price2}$")
    elif question1 == Prod3 and question2 >= price1:
        print(f"{Prod3}_{mob1}_{price1}$")
    else:
        print("Unfortunately, you don't have the budget")
else:
    print("Incorrect type of product or you don't have the budget")
 


#task N3

print("Task_N3")

a = "1. Beer and beer attributes; "
b = "2. Products for dinner;"
c = "3. Baby food"
d = 50
e = 100
f = 150
g = 'yes'
h = 'no'

print("Please indicate your choice with a number...")

question1 = int(input(f"You should purchase a basket of products that fully meet your needs.\n\
Which basket will you buy?\n {a} \n {b} \n {c} \n "))

question2 = int(input(f"How much money are you going to spend? \n {d} \n {e} \n {f} \n"))

if question1 == 1 and (question2 >= e or question2 >= f):
    print("You can buy it")

elif question1 == 2 and (question2 >= e or question2 >= f):
    print("You can buy it")

elif question1 == 3 and (question2 >= e or question2 >= f):
    print("You can buy it")
else:
    print("You don't have enough money!")
    question3 = input(f"Will you add the amount? \n {g} \n {h} \n").lower().strip()

    if question3 == g:
        question4 = int(input("how much? "))
        if question4 + question2 >= e:
            print("You can buy it")
        else:
            print("You don't have enough money!")
    else:
        print("Have a good day!")

#task 4

print("Task_N4")

a = 'yes'
b = 'no'
print("Welcome to Recommender! ")

question1 = input(f"Do you enjoy working with technology and solving complex problems? ({a}/{b}) - ").lower().strip()
question2 = input(f"Do you enjoy working with people and helping them? ({a}/{b}) - ").lower().strip()
question3 = input(f"Do you prefer working outdoors and being physically active? ({a}/{b}) - ").lower().strip()

if question1 == a and question2 == b and question3 == b:
    print("You might enjoy a career in IT or programming.")

elif question1 == b and question2 == a and question3 == b:
    print("You might enjoy a career in customer service or counseling.")

elif question1 == b and question2 == b and question3 == a:
    print("You might enjoy a career in landscaping or outdoor activities.")

elif question1 == a and question2 == a and question3 == b:
    print("You might enjoy a career in sales or marketing.")

elif question1 == a and question2 == b and question3 == a:
    print("You might enjoy a career in engineering or construction.")
else:
    print("Based on your preferences, it's challenging to recommend a specific profession. Consider exploring different options.")