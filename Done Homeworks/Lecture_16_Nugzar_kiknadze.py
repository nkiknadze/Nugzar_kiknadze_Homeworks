#Task_N1
'''
1.	შექმენი წრის კლასი, რომელსაც ექნება მეთოდები საკუთარი პერიმეტრისა და ფართობის გამოსათვლელად.
'''
print("Task_N1")

π = 3.14
radius = int(input("Enter the radius of the circle: "))

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def cal_perimeter(self):
        return 2 * π * self.radius

    def cal_area(self):
        return π * self.radius**2

circle_instance = Circle(radius)

perimeter_result = circle_instance.cal_perimeter()
area_result = circle_instance.cal_area()

print(f"Circle with radius {radius} 'cm' ")
print(f"Perimeter is: {perimeter_result:.2f}")
print(f"Area is: {area_result:.2f}")
print()

#Task_N2
'''
2.შექმენი კალკულატორის კლასი, საბაზისო არითმეტიკული ოპერაციების მეთოდებით.
'''
print("Task_N2")

class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

calculator_instance = Calculator()
x = int(input("Enter the value 'X': "))
y = int(input("Enter the value 'Y': "))

result_add = calculator_instance.add(x, y)
result_subtract = calculator_instance.subtract(x, y)
result_multiply = calculator_instance.multiply(x, y)
result_divide = calculator_instance.divide(x, y)

print(f"Addition is: {result_add}")
print(f"Subtraction is: {result_subtract}")
print(f"Multiplication is: {result_multiply}")
print(f"Division is: {result_divide}")
print()

#Task_N3
'''
3.შექმენი შოფინგის კალათის კლასი, რომელსაც ექნება მეთოდები სასურველი ნივთის დასამატებლად და ამოსაშლელად,
ასევე კალათაში არსებული პროდუქტების სიისა და ჯამური ღირებულების გამოსატანად. 
'''
print("Task_N3")

class ShoppingCart:
    def __init__(self):
        self.items = {}
    def add_item(self, item, price, quantity):
        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if quantity >= self.items[item]["quantity"]:
                del self.items[item]
            else:
                self.items[item]["quantity"] -= quantity

    def display_cart(self):
        if not self.items:
            print("The shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item, details in self.items.items():
                print(f"{item}: {details['quantity']} x ${details['price']:.2f}")
            total_cost = sum(details["price"] * details["quantity"] for details in self.items.values())
            print(f"Total Cost: ${total_cost:.2f}")

cart_instance = ShoppingCart()

a = "yes"

while True:
    if a == 'no':
        break 
    else:
        name = input("Enter the product name: ")
        price = float(input("Enter the price: "))
        quantity = int(input("Enter quantity: "))
        cart_instance.add_item(name, price, quantity)
        a = input("Continue? (yes/no) ").lower()
        
cart_instance.display_cart()
