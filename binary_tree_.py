class node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree(object):
    def __init__(self, root):
        self.root = node(root)

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
            return self.preorder_print(tree.root, "").strip("-")
        if type == "inorder":
            return self.inorder_print(tree.root, "").strip("-")        
        if type == "postorder":
            return self.postorder_print(tree.root, "").strip("-")
        
tree = Binary_Tree(1)
tree.root.left = node(2)
tree.root.right = node(3)
tree.root.left.left = node(4)
tree.root.left.right = node(5)
tree.root.right.left = node(6)
tree.root.right.right = node(7)
tree.root.right.right.right = node(8)

print(tree.printtree("preorder"))
print(tree.printtree("inorder"))
print(tree.printtree("postorder"))
