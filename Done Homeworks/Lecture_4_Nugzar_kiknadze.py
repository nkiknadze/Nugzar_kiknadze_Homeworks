#taskN1

print("Task_N1")
def count_characters(sentence):
    num_count = 0
    alpha_count = 0
    symbol_count = 0

    for char in sentence:
        if char.isdigit():
            num_count =num_count + 1
        elif char.isalpha():
            alpha_count =alpha_count + 1
        else:
            symbol_count =symbol_count + 1

    return num_count, alpha_count, symbol_count

user_input = input("please input the sentences: ")
num, alpha, symbol = count_characters(user_input)

print("Count of numbers:", num)
print("Count of letters of the alphabet:", alpha)
print("Count of symbols:", symbol)

print()

#task_N2
print("Task_N2")

def sentence(sentence1, sentence2):
    if len(sentence1) > 0 and len(sentence2) > 0:
        new_sentence = sentence1[0] + sentence2[-1] + sentence1[1] + sentence2[-1]
        return new_sentence
    else:
        return "Please enter valid sentences."

sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

new_result = sentence(sentence1, sentence2)
print("NEW Sentence:", new_result)

print()

#task_N3
print("Task_N3")

def balance(sentence1, sentence2):

    condition1 = True
    for char in sentence1:
        if char not in sentence2:
            condition1 = False
            break
    condition2 = True
    for char in sentence2:
        if char not in sentence1:
            condition2 = False
            break

    return condition1 and condition2

sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

if balance(sentence1, sentence2):
    print("Strings are balanced!")
else:
    print("Strings are not balanced!")
