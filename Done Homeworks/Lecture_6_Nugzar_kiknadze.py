
#_______________
#Task_N1
#_______________
'''
1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს და დაბეჭდავს შემდეგნაირად:
input: “
Output: Tripled: ablabdabdabablabdabdabablabdabdab
'''
print("Task_N1")

num = 3
def trip():
    ask = input("Please enter the word: ")
    result = ask*num
    return result

print(f"''Tripled: {trip()}''")
print()

#_______________
#Task_N2
#_______________

'''
2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)
'''
print ("Task_N2")

earth_weight = 0

def moon_weight(earth_weight):
    moon_gravity = 1 / 6
    weight_on_the_moon = earth_weight * moon_gravity
    return weight_on_the_moon
earth_weight =float(input("Enter your weight on Earth: "))
print(f"Your weight on the moon would be: {round(moon_weight(earth_weight),2)}")
print()

#_______________
#Task_N3
#_______________
'''
3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს, მოქმედებას (+ - * / ^), მეორე რიცხვს)
მაგ. „2 * 6“. ფუნქცია დაშლის სტრიქონს split() ფუნქციის გამოყენებით. დათვლის და დააბრუნებს შედეგს. 
გაითვალისწინე რომ რიცხვის შეყვანის მაგიერ სიმბოლოების შეყვანის შემთხვევაში უნდა დააბრუნოს ფუნქციამ შესაბამისი მესიჯი. 
ასევე ნულზე გაყოფა არ შეიძ₾ება, ამ შემთხვევაშიც უნდა დააბრუნოს შესაბამისი მესიჯი. (დააბრუნოს და არა დაპრინტოს)
'''
print("Task_N3")

def simple_calculator():
    user_input = input("Enter a mathematical expression (e.g., '2 * 6'): ")
    parts = user_input.strip().split()

    if len(parts) != 3:
        return "Error: Invalid input. Please enter a valid expression."
    
    num1_str, operator, num2_str = parts

    if not num1_str.isnumeric() or not num2_str.isnumeric():
        return "Error: Invalid input. Please enter numeric values."
    num1 = float(num1_str)
    num2 = float(num2_str)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        result = num1 / num2
    elif operator == '^':
        result = num1 ** num2
    else:
        return "Error: Invalid operator."
    return round(result,2)

print(f"Result is: {simple_calculator()}")
print()

#_______________
#Task_N4
#_______________

'''
გავლილი მასალის გამოყენებით შექმენი ფუნქცია, რომელიც მიიღებს ლათინური სიმბოლოებით დაწერილ სიტყვას, დაშიფრავს მორწეს ანბანით და დააბრუნებს შედეგს.
'''

print("Task_N4")

word = 'SOS'
def latin_to_morse(word):
    latin_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..'
                  , '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', ' ']
    word = word.upper()
    morse_result = ' '.join([morse_code[latin_chars.index(char)] for char in word if char in latin_chars])
    return morse_result
word = input("Enter a word in Latin characters: ")
morse_code = latin_to_morse(word)

print(f"Morse code for '{word}' is: {morse_code}")
print()
