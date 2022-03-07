'''
删除二叉搜索树中的一个节点
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def successor(node):
    node = node.right
    while node.left != None:
        node = node.left
    return node.val


def pre_successor(node):
    node = node.left
    while node.right != None:
        node = node.right
    return node.val


def delete_node(root, key):
    if not root:
        return None

    if root.val == key:
        if not root.left and not root.right:
            root = None
        elif root.left:
            root.val = pre_successor(root)
            root.left = delete_node(root.left, root.val)
        else:
            root.val = successor(root)
            root.right = delete_node(root.right, root.val)
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:
        root.left = delete_node(root.left, key)

    return root
