#Task_N1
'''
1. დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე ლექსიკონს დააბრუნებს.
'''
print("Task_N1")

def remove_duplicates(a):
    unique_dict = {}
    seen_values = set()

    for key, value in a.items():
        if value not in seen_values:
            unique_dict[key] = value
            seen_values.add(value)

    return unique_dict

dict2 = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2 , 'f':5}
result_dict = remove_duplicates(dict2)
print(result_dict)
print()

#Task_N2
'''
2.დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.
'''
print("Task_N2")

def is_dict_empty(a):
    if not a:
        return "Empty"
    else:
        return "Not Empty"

b = {"Test":1}
result = is_dict_empty(b)
print(result)
print()

#Task_N3
'''
3. დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს.
ვთქვათ გადავეცით ფუნქციას სტრიქონი, უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და მათი რაოდენობა value_ს ადგილას.
მაგალითად გადავეცით სტრიქონი : 'racoon'
უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}
'''
print("Task_N3")

def create_dict(a):
    char_dict = {}
    
    for char in a:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

input = 'tavsatekhi'
result = create_dict(input)
print(result)
print()
