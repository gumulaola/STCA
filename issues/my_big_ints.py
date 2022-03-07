'''
给出 n 个整数 找出一组组合使和最大 不能相邻
[1,100,2,3,200]
[100,200]
'''


input = [1, 100, 2, 3, 200]


def solution(nums):
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0]
    for i in range(2, len(nums)+1):
        dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])
    return dp[-1]


print(solution(input))
