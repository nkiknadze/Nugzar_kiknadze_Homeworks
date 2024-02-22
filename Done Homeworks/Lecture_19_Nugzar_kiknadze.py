
#პირველი სია, სადაც არის მნიშვნელობა და შემდგომი მნიშვნელობა (თავდაპირველად არის ნან).
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

#დაკავშირებული სია, სადაც არის პირველი სიის მნიშვნელობა და სიის რაოდენობა, პირვეი ჩანაწერი რადგან არის შესაბამისად რაოდენობაც არის 1.
class LinkedList:
    def __init__(self, value):
        self.head = ListNode(value)
        self.length = 1

#მეთოდი დაკავშირებულ სიის ბოლოში ამატებს მნიშვნელობას, თუ სია ცარიელია ამატებს პირველ მნიშვნელობად.
    def append(self, value):
        current_node = self.head

        # ვაილ ციკლი მუშაობს მანამ სანამ არ მივა ბოლო მნიშვნელობასთან სადაც შემდგომი ნოუდი არის ნან-ი
        while current_node.next is not None:
            current_node = current_node.next

        # იქმნება ახალი ნოუდი რომელიც ემატება სიის ბოლო მნიშვნელობის შემდგომ მნიშვნელობას. ასვეე ყოველი ჩანაწერის შემდგომ ზრდის +1 ით რაოდენობას.
        new_node = ListNode(value)
        current_node.next = new_node
        self.length += 1

# ინსერტ მეთოდით ხდება მნიშვნელობის ჩამატება მითითებულ ადგილას.
    def insert(self, value, index):
        last_index = self.length - 1  #ბოლო მნიშვნელობის იდენტიფიცირება (რაოდენობას გამოკლებული -1)
        i = 0

        if index == 0: # თუ ცალიელია მაშინ იწყებს პირველი მნიშვნელობით ჩასმას.
            old_head = self.head
            self.head = ListNode(value)
            self.head.next = old_head
            self.length += 1 #ყოველი დამატების შემდგომ ამატებს +1 რაოდენობაში.

        elif index == last_index + 1: #თუ ინდექსი უდრის ბოლო მნიშვნელობას მაშნ გამოიყენება აპპენდ 
                                    #და დამატება ხდება ბოლოში (რომელშიც თავის თავად არის უკვე გაწერილი ბოლო რაოდენობაში +1 დამატება)
            self.append(value) 

            #მნიშვნელობის დამატება როდესაც დამატება არ ხდება თავში და ბოლოში.  (ამის ლოგიკის გარჩევის შანსი არაა :))
        elif 0 < index < last_index + 1:
            current_node = self.head
            while i != index - 1:
                current_node = current_node.next
                i += 1

            new_node = ListNode(value)
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

        elif index > last_index + 1 or index < 0: # არარსებული ინდექსის იდენტიფიცირება, გამოდის შესაბამისი მესიჯი
            print("Index is out of range...")

        #მნიშვნელობის წაშლა.
    def remove(self, index):
        last_index = self.length - 1
        i = 0

        if index == 0: # პირველი მნიშნელობის წაშლა (მარტივი), წაშლის შემდგომ რაოდენობაში აკლდება -1
            self.head = self.head.next
            self.length -= 1 

        elif index == last_index: # ბოლო მნიშნელობის წაშლა (მარტივი), წაშლის შემდგომ რაოდენობაში აკლდება -1
            current_node = self.head
            while i < last_index - 1:
                current_node = current_node.next
                i += 1

            current_node.next = None
            self.length -= 1

        elif 0 < index < last_index: #მნიშვნელობის წაშლა როდესაც წასაშლელი არ არის თავში ან ბოლოში. (ამის ლოგიკის გარჩევის შანსი არაა :))
            current_node = self.head
            while i != index - 1:
                current_node = current_node.next
                i += 1

            deleted_element = current_node.next
            current_node.next = deleted_element.next
            self.length -= 1

        elif index > last_index + 1 or index < 0: # არარსებული ინდექსის იდენტიფიცირება, გამოდის შესაბამისი კოდი
            print("Index is out of range...")

    def printList(self):
        current_node = self.head
        print(f"{current_node.value} ->", end='')  #პირველი მნიშველობის დაბეჯდვა, ხოლო შემდგომ დაბეჭდება ვაილ ციკლის მეშვეობით ყველა მნიშვნელობა
                                                    #სანამ ბოლო მნიშნელობის, შემდგომი მნიშვნელობა არ იქნება ნან-ი
        while current_node.next is not None:
            current_node = current_node.next
            print(f" {current_node.value} ->", end='')  


#ფუნქციების გამოძახება და დაბეჭდვა (კოდი მუშაობს)
linked_list = LinkedList(1)
linked_list.append(3)
linked_list.insert(2, 1)
linked_list.append(4)
linked_list.remove(0)
linked_list.printList()
