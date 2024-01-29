#Task_N1
'''
1.	დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.
'''
print("Task_N1")

import re
import csv
import os
from collections import Counter

def find_word(a):

    with open(r'C:\Users\nkiknadze\Desktop\Python Cource 2023\article.txt', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        text = ' '.join([' '.join(row) for row in reader]) # -- ეს ნაწილი ვერ გავიგე და ნიკას უნდა ვკითხო ლექციაზე.

    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()

    word_counts = Counter(words)
    second_word, count = word_counts.most_common(2)[-1]

    return second_word, count

result, count = find_word(r'C:\Users\nkiknadze\Desktop\Python Cource 2023\article.txt')
print(f"ganmeorebis raodenobit meorea '{result}' da aris {count} - jer gameorebuli.")
print()

#Task_N2
'''
2.	names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.
'''
print("Task_N2")

csv_file_path = r"C:\Users\nkiknadze\Desktop\Python Cource 2023\names.csv"

csv_directory = os.path.dirname(csv_file_path)
txt_file_path = os.path.join(csv_directory, "names.txt")
with open(csv_file_path, mode='r') as csv_file, open(txt_file_path, mode='w') as txt_file:
    csv_reader = csv.DictReader(csv_file)
    txt_file.write(f"first_name last_name email\n")
    
    for row in csv_reader:
        full_name = f"{row['first_name']} {row['last_name']}"
        email = row['email']
        txt_file.write(f"{full_name} {email}\n")

print(f"monacemebi dakopirda {csv_file_path} dan {txt_file_path} shi warmatebit.")
print()
