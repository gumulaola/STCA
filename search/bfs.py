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


def bfs():
    queue = [[0, 0, 0, 0]]

    while queue:
        peek = queue.pop(0)
        i, j, k, step = peek

        if maze[i][j][k] == "E":
            return step

        for index in range(6):
            ii = i + directions[index][0]
            jj = j + directions[index][1]
            kk = k + directions[index][2]

            if ii < 0 or ii >= h or jj < 0 or jj >= m or kk < 0 or kk >= n or maze[ii][jj][kk] == "#" or vis[ii][jj][kk]:
                continue

            vis[ii][jj][kk] = True
            queue.append([ii, jj, kk, step+1])

    return -1


# Main
print(bfs(0, 0, 0, 0))
