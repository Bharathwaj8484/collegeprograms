class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        ele=[]
        cur = self.head
        while cur.next != None:
            cur = cur.next
            ele.append(cur.data)
        print(ele)

    def get(self,index):
        if index >= self.length():
            print("Error! out of range")
            return " "
        id=0
        cur = self.head
        while True:
            cur = cur.next
            if id == index:
                return cur.data
            id +=1 

    def deleteid(self,index):
        if index >= self.length():
            print("Error! out of range")
            return " "
        id = 0 
        cur = self.head
        if index == 0:
            self.head = cur.next
            return
        while True:
            last = cur
            cur = cur.next
            id +=1
            if id == index:
                last.next = cur.next
                return
            
    def deleteval(self,val):           
        cur = self.head
        while cur.next != None:
            last = cur
            cur = cur.next
            if cur.data == val:
                last.next = cur.next
                return 
        return "Not Found"



ll=Linkedlist()
ll.append(3)
ll.append(8)
ll.append(7)
ll.append(2)
ll.append(5)
ll.append(4)
ll.display()
# print(ll.length())
# print(ll.get(8))

ll.deleteid(2)
ll.display()
ll.deleteval(8)
ll.display()