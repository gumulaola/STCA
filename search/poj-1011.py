'''
problem link: http://poj.org/problem?id=1011
NOTE 主要体现剪枝思想

Example input:
9
5 2 1 5 2 1 5 2 1
Example output:
6

f(n, len, rLen)
n: 剩余多少个零件未使用
len: 预计原始长度
rLen: 当前正在拼的那一段还剩多少没拼完
return: True or False
'''

nums_len = int(input())

nums = input().split()
nums = [int(num) for num in nums]

vis = [False]*nums_len


def dfs(n, len, rLen, index):
    if n == 0 and rLen == 0:
        return True

    if rLen == 0:
        rLen = len
        index = 0

    pre = 0
    for i in range(index, nums_len):
        if (
            rLen < nums[i]  # 当前剩余不足放下当前小棍
            or vis[i]  # 已经访问过
            or nums[i] == pre  # 这种零件长度已经试过了不行 跳过
        ):
            continue

        vis[i] = True
        if dfs(n-1, len, rLen-nums[i], index+1):
            vis[i] = False
            return True
        vis[i] = False

        if rLen == len or rLen == nums[i]:
            break

        pre = nums[i]

    return False


nums.sort()
nums.reverse()
for len in range(nums[0], sum(nums)+1):
    if sum(nums) % len == 0:
        if dfs(nums_len, len, len, 0):
            print(len)
            break
