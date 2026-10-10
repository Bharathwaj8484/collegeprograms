class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, data, cur=None):
        if self.root is None:
            self.root = Node(data)
        else:
            if cur is None:
                cur = self.root
            if data < cur.data:
                if cur.left is None:
                    cur.left = Node(data)
                else:
                    self.insert(data, cur.left)
            elif data > cur.data:
                if cur.right is None:
                    cur.right = Node(data)
                else:
                    self.insert(data, cur.right)
            else:
                print("Value already in Tree")
                

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return 1 + max(left_height, right_height)

    def search(self, data, cur=None):
        if cur is None:
            cur = self.root
        if cur is None:
            return False  
        if data == cur.data:
            return True
        elif data < cur.data and cur.left is not None:
            return self.search(data, cur.left)
        elif data > cur.data and cur.right is not None:
            return self.search(data, cur.right)
        return False 


    def preorder_print(self, node, trav_str):
        if node:
            trav_str += (str(node.data) + "-")
            trav_str = self.preorder_print(node.left, trav_str)
            trav_str = self.preorder_print(node.right, trav_str)
        return trav_str

    def inorder_print(self, node, trav_str):
        if node:
            trav_str = self.inorder_print(node.left, trav_str)
            trav_str += (str(node.data) + "-")
            trav_str = self.inorder_print(node.right, trav_str)
        return trav_str

    def postorder_print(self, node, trav_str):
        if node:
            trav_str = self.postorder_print(node.left, trav_str)
            trav_str = self.postorder_print(node.right, trav_str)
            trav_str += (str(node.data) + "-")
        return trav_str

    def printtree(self, type):
        if type == "preorder":
            return self.preorder_print(self.root, "").strip("-")
        if type == "inorder":
            return self.inorder_print(self.root, "").strip("-")        
        if type == "postorder":
            return self.postorder_print(self.root, "").strip("-")

def fill_tree(tree):
    from random import randint
    for _ in range(100):
        val = randint(0, 1000)
        tree.insert(val)
    return tree

tree = BinaryTree()
tree = fill_tree(tree)
print("Height: ", tree.height(tree.root))
print("Search for 500:", tree.search(25))
print("\nPreorder:\n", tree.printtree("preorder"))
print("\nInorder:\n", tree.printtree("inorder"))
print("\nPostorder:\n", tree.printtree("postorder"))
