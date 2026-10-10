class node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = node()
        
    def append(self,data):
        new_node=node(data)
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
        ele = []
        curn = self.head
        while curn.next != None:
            curn = curn.next
            ele.append(curn.data)
        print(ele)
    
    def get(self,id):
        if id >= self.length():
            print("ERROR: 'id' is larger than the linked list length.")
            return None
        curnid = 0
        curn = self.head
        while True:
            curn = curn.next 
            if curnid == id:
                return curn.data
            curnid += 1
    
    def deleteindex(self,id):
        if id >= self.length():
            print("ERROR: 'id' is larger than the linked list length.")
            return None
        curnid = 0
        curn = self.head
        while True:
            lastnode = curn
            curn = curn.next
            if curnid == id:
                lastnode.next = curn.next
                return
            curnid+=1

    def deletedata(self,d):
        curn = self.head
        while curn.next!=None:
            lastnode = curn
            curn = curn.next
            if curn.data == d:
                lastnode.next = curn.next
                return
        return "not found"
 
ll=linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()

# a=ll.deletedata(5)
# ll.display()
# print(a)
# # print ("ele at 2nd index: %d" % ll.get(2))
# ll.display()

class LinkedListSum:
    @staticmethod
    def add_lists(list1, list2):
        # Create a new linked list for storing the result
        result_list = linkedlist()
        cur1 = list1.head.next  # Skip the dummy head node
        cur2 = list2.head.next  # Skip the dummy head node

        while cur1 is not None and cur2 is not None:
            # Add data of current nodes from both lists
            sum_value = cur1.data + cur2.data
            # Append the sum to the result linked list
            result_list.append(sum_value)
            # Move to the next nodes
            cur1 = cur1.next
            cur2 = cur2.next

        return result_list

# Example Usage
# Creating first linked list
ll1 = linkedlist()
ll1.append(1)
ll1.append(2)
ll1.append(3)

# Creating second linked list
ll2 = linkedlist()
ll2.append(10)
ll2.append(10)
ll2.append(10)

# Adding the two lists
result = LinkedListSum.add_lists(ll1, ll2)

# Displaying the resulting list
result.display()  # Output: [5, 7, 9]
