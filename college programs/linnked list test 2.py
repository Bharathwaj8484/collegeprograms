class node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head=node()

    def insert(self,data):
        new_node=node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        ele=[]
        cur=self.head
        while cur.next != None:
            cur = cur.next
            ele.append(cur.data)
        print(ele)

    def length(self):
        t=0
        cur = self.head
        while cur.next != None:
            cur= cur.next
            t+=1
        return t

    def get(self,index):
        if index >= self.length():
            print("error")
            return ""
        id = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            id +=1
            if id == index:
                print (int(cur.data))

    def deleteid(self,index):
        if index >= self.length():
            print("error")
            return ""
        id = 0
        cur = self.head
        if index == 0:
            self.head = cur.next
            return
        while cur.next != None:
            last = cur
            cur = cur.next
            id +=1
            if id == index:
                last.next = cur.next

    def deleteval(self,value):
        cur = self.head
        while cur.next != None:
            last = cur
            cur = cur.next
            if cur.data == value:
                last.next = cur.next



ll=LinkedList()
ll.insert(1)
ll.insert(7)
ll.insert(8)
ll.insert(9)
ll.insert(2)
ll.display()
print(ll.length())
ll.get(2)
ll.deleteval(8)
ll.display()

