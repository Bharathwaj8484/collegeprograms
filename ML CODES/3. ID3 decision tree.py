class Node:
    def __init__(self, attribute=None, value=None, results=None, true_branch=None, false_branch=None):
        self.attribute, self.value, self.results, self.true_branch, self.false_branch = attribute, value, results, true_branch, false_branch
def build_tree(rows):
    if not rows:
        return Node()
    if len(set(row[-1] for row in rows)) == 1:
        return Node(results=rows[0][-1])
    num_attributes = len(rows[0]) - 1
    best_attribute = max(range(num_attributes), key=lambda col: information_gain(rows, col))
    true_rows = [row for row in rows if row[best_attribute] == 'Yes']
    false_rows = [row for row in rows if row[best_attribute] == 'No']
    true_branch = build_tree(true_rows)
    false_branch = build_tree(false_rows)
    return Node(attribute=best_attribute, value=rows[0][best_attribute], true_branch=true_branch, false_branch=false_branch)
def information_gain(rows, col):
    total_entropy = entropy(rows)
    values = set(row[col] for row in rows)
    weighted_entropy = sum(len(list(filter(lambda row: row[col] == val, rows))) / len(rows) * entropy(list(filter(lambda row: row[col] == val, rows))) for val in values)
    return total_entropy - weighted_entropy
def entropy(rows):
    from math import log2
    counts = class_counts(rows)
    return -sum(count / len(rows) * log2(count / len(rows)) for count in counts.values())
def class_counts(rows):
    return dict((row[-1], rows.count(row)) for row in rows)
dataset = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes']
]
tree = build_tree(dataset)
def print_tree(node, indent=""):
    if node is None:
        return
    if node.results is not None:
        print(indent + str(node.results))
    else:
        print(indent + f'Attribute {node.attribute} : {node.value}? ')
        print(indent + '--> True:')
        print_tree(node.true_branch, indent + '  ')
        print(indent + '--> False:')
        print_tree(node.false_branch, indent + '  ')
print_tree(tree)
new_sample = ['Sunny', 'Cool', 'High', 'Strong']
current_node = tree
while current_node.results is None and current_node.attribute is not None:
    if new_sample[current_node.attribute] == current_node.value:
        current_node = current_node.true_branch
    else:
        current_node = current_node.false_branch
print(f"\nClassification result for {new_sample}: {current_node.results}")
