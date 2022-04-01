numbers = [3, 2, 1, 5, 6, 4]


def max_heapify(nums, start, end):
    dad = start
    son = start*2 + 1
    while son <= end:
        if son + 1 <= end and nums[son] < nums[son+1]:
            son += 1
        if nums[son] < nums[dad]:
            return
        else:
            nums[son], nums[dad] = nums[dad], nums[son]
            dad = son
            son = dad*2 + 1


def heap_max_k(nums, k):
    lens = len(nums)
    for i in range(lens//2 - 1, -1, -1):
        max_heapify(nums, i, lens-1)
    for j in range(k):
        nums[lens-1-j], nums[0] = nums[0], nums[lens-1-j]
        max_heapify(nums, 0, lens-2-j)
    return nums[lens-k]


print(heap_max_k(numbers, 2))
