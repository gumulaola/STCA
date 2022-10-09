'''
3 4 5
S....
.###.
.##..
###.#

#####
#####
##.##
##...

#####
#####
#.###
####E
'''

h, m, n = map(int, input().split())


# NOTE 数据范围
N = 30

# NOTE 初始化三维矩阵 代表迷宫
maze = [[[0]*N for _ in range(N)] for _ in range(N)]

# NOTE 初始化三维矩阵 代表迷宫每个坐标是否访问过
vis = [[[0]*N for _ in range(N)] for _ in range(N)]

# NOTE 6个方向
directions = [[1, 0, 0], [-1, 0, 0], [0, 1, 0],
              [0, -1, 0], [0, 0, 1], [0, 0, -1]]


def dfs(i, j, k):  # 返回由 点(i,j,k) 到达终点需要多少步
    if maze[i][j][k] == "E":
        return 0

    nxt = float("+inf")

    for index in range(6):
        ii = i + directions[index][0]
        jj = j + directions[index][1]
        kk = k + directions[index][2]

        if ii < 0 or ii >= h or jj < 0 or jj >= m or kk < 0 or kk >= n or maze[ii][jj][kk] == "#" or vis[ii][jj][kk]:
            continue

        vis[ii][jj][kk] = True
        nxt = min(nxt, dfs(ii, jj, kk))
        vis[ii][jj][kk] = False

    return nxt if nxt == float("+inf") else nxt + 1


# Main
print(dfs(0, 0, 0))
