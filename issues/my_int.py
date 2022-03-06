'''
给出一个 int 数组 找出没有出现在数组中的最大负整数
->> 取负操作
->> 给出一个 int 数组 找出没有出现在数组中的第一个正整数 (第一个缺失的正整数)
[-2, 1, 2, 3]
[2, -1, -2, -3]
'''

# output will be -1
input = [-2, 1, 2, 3]


def solution(nums):
    for i in range(len(nums)):
        nums[i] = -nums[i]

    # [2, -1, -2, -3]

    my_dict = {}
    for i in range(len(nums)):
        if nums[i] <= 0:
            pass
        else:
            my_dict[nums[i]] = True

    for i in range(1, len(nums)+1):
        if i not in my_dict:
            return -i

    return -(len(nums+1))


print(solution(input))
