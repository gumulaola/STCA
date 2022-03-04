# Definition for singly-linked list.
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def build_list(numbers):
    fake_head = ListNode(1000)
    prev = fake_head
    for i in range(len(numbers)):
        node = ListNode(numbers[i])
        prev.next = node
        prev = node
    head = fake_head.next
    return head


numbers = [10, 2, 40, 3, 4, 6, 12, 32, 1, 8]
head = build_list(numbers)
