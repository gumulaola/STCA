# Definition for a binary tree node.
from platform import node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(numbers, index):
    if index >= len(numbers):
        return None
    if numbers[index] == None:
        return None
    root = TreeNode(numbers[index])
    left_index = 2*index + 1
    right_index = 2*index + 2
    root.left = build_tree(numbers, left_index)
    root.right = build_tree(numbers, right_index)
    return root


'''
        3
    9       20
        15      7
'''

numbers = [3, 9, 20, None, None, 15, 7]
root = build_tree(numbers, 0)


def serialize(root):
    if not root:
        return "null"

    left = serialize(root.left)
    right = serialize(root.right)

    return str(root.val) + "," + left + "," + right


print(serialize(root))


def deserialize(data):
    data = data.split(",")

    def build(data):
        if not data:
            return None

        cur = data.pop(0)
        if cur == "null":
            return None

        node = TreeNode(int(cur))
        node.left = build(data)
        node.right = build(data)

        return node

    root = build(data)
    return root
