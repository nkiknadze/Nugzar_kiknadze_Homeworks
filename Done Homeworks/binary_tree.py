
#Task_N1

'''
1.	მოიძიე ბინარული ხის მონაცემთა სტრუქტურის კოდი და დააკომენტარე. (Binary Tree Data Structure in Python)

2. მოიფიქრეთ შუალედური პროექტის იდეა და დაიწყეთ მუშაობა

'''
#Task_N2
# შუალედურ პროექტისთვის ვფიქრობ გავაკეთო სესხის ანუიტეტის პროგრამა, რომელიც მიიღებს გარკვეულ მნიშნელობებს და თვეების მიხედვით ააწყობს
# სესხის გადახდის გრაფიკს (ძირი, პროცენტი, ჯამი) ასევე დააჯამებს სრულ თანხებს პერიოდის ბოლში.
# პროგრამას უნდა შეეძლოს ფაილის გენერირება და დასაბეჭდ ფორმაში დაექსპორტება (Ecxel or PDF რომელიც მარტივად გამომივა).

#ახალი ნოდის შექმნ, ქმნის მნიშვნელობას, მარცხენა და მარჯვენა კავშირს შემდგომი მნიშნელობისთვის (თავიდან ნან-ია) 
print("Task_N1\n")
class Node:
    def __init__(self, data):
        self.data = data 
        self.leftChild = None  
        self.rightChild = None


    # ინსერტის ფუნქცია, რომელიც ამატებს ელემენტს იმის მიხედვით მეტია თუ არა შვილობილი მნიშვნელობა ძირითადთან შედარებით.
    def insert(self, data):
        # თუ ახალი მნიშვნელობა ნაკლებია მშობელ მნიშნელობაზე მოძრაობს მარცხნივ და ამატებს მნიშნელობას
        if data < self.data:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        # თუ ახალი მნიშვნელობა მეტია მშობელ მნიშნელობაზე მოძრაობს მარჯვნივ და ამატებს მნიშნელობას
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return

    # ხის გამოტანის ფუნქცია
    def PrintTree(self):
        if self.leftChild:
            # მარცხენა განშტოების მეჭდვა
            self.leftChild.PrintTree()
        print(self.data) 
        if self.rightChild:
            # მარჯვენა განშტოების მეჭდვა
            self.rightChild.PrintTree()

# მშობელი მნიშვნელობის შექმნა
root = Node(1)
# ახალი მნიშვნელობების დამატება, რომლებიც განლაგდება მარცნივ ან მარჯვნივ და დაიბეჭდება ზრდადობით.
root.insert(5)
root.insert(12)
root.insert(2)
root.insert(3)
root.insert(22)

root.PrintTree()
print()
