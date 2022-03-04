# Implementation of a max heapq
class my_heap():
    def __init__(self):
        self.arr = []

    def my_pop(self):
        head = self.arr[0]
        self.arr[0] = self.arr[len(self.arr)-1]
        del self.arr[len(self.arr)-1]
        dad = 0
        son = 1
        while son < len(self.arr):
            if son+1 < len(self.arr) and self.arr[son+1] > self.arr[son]:
                son += 1
            if self.arr[dad] > self.arr[son]:
                return head
            else:
                self.arr[dad], self.arr[son] = self.arr[son], self.arr[dad]
                dad = son
                son = dad*2 + 1
        return head

    def my_push(self, val):
        self.arr.append(val)
        lens = len(self.arr)
        dad = lens//2 - 1
        son = lens - 1
        while dad >= 0:
            if self.arr[dad] < self.arr[son]:
                self.arr[dad], self.arr[son] = self.arr[son], self.arr[dad]
                son = dad
                dad = (son-1)//2
            else:
                break
        return 0


# Test
test = my_heap()
nums = [3, 4, 2, 1000, 7, 8, 100]
for i in nums:
    test.my_push(i)
for i in range(len(test.arr)):
    print(test.my_pop())
