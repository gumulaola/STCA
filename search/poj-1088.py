'''
NOTE 记忆化搜索
一个人可以从某个点滑向上下左右相邻四个点之一 当且仅当高度减小
5 5
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''

m, n = map(int, input().split())

N = 30
maze = [[0]*N for _ in range(N)]
dp = [["null"]*N for _ in range(N)]
directions = [[1, 0], [-1, 0][0, 1], [0, -1]]


def dfs(i, j):
    if dp[i][j] != "null":
        return dp[i][j]

    nxt = 0
    for index in range(4):
        ii = i + directions[index][0]
        jj = j + directions[index][1]

        if ii < 0 or ii >= m or jj < 0 or jj >= n or maze[ii][jj] >= maze[i][j]:
            continue

        nxt = max(nxt, dfs(ii, jj))

    dp[i][j] = nxt + 1
    return dp[i][j]

# Main


ans = 0

for i in range(m):
    for j in range(n):
        ans = max(ans, dfs(i, j))
