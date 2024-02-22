#Task_N1
'''
1. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით (გამოიყენე set მონაცემთა ტიპი).
def unique_list():
    ...
    return ...
'''
print("Task_N1")

def unique_list(list1):
    unique_elements = list(set(list1))
    return unique_elements

list1 = [1, 2, 2, 3, 4, 4, 5,'a','b','c','c','d','d','d','d']
result_list = unique_list(list1)
print(result_list)
print()

#Task_N2
'''
2. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით, რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).
def immutable_set():
    ...
    return ...
'''
print("Task_N2")

def immutable_set(list1):
    return frozenset(list1)

list1 = [1, 2, 2, 3, 4, 4, 5,'a','b','c','c','d','d','d','d']
result_set = immutable_set(list1)
print(result_set)
print()

#Task_N3
'''
3. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს tuple ტიპის მონაცემად და დააბრუნებს შედეგს.
def set_to_tuple():
    ...
    return ...
'''
print("Task_N3")

def set_to_tuple(set1, set2):
    combined_set = set1.union(set2)
    result_tuple = tuple(combined_set)
    return result_tuple

set_a = {1, 2, 3, 3, 3}
set_b = {3, 4, 5, 5, 5}
result_tuple = set_to_tuple(set_a, set_b)
print(result_tuple)
print()



