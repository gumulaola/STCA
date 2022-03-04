# Definition for a binary tree node.
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


numbers = [3, 9, 20, None, None, 15, 7]
root = build_tree(numbers, 0)
