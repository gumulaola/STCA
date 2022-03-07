'''
用一个链表实现队列
'''


class linked_list:
    def __init__(self, val):
        self.val = val
        self.next = None


class my_queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        if not self.head:
            self.head = linked_list(val)
            self.tail = self.head
        else:
            self.tail.next = linked_list(val)
            self.tail = self.tail.next

    def pop(self):
        if not self.head:
            return None
        else:
            temp = self.head
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            return temp
