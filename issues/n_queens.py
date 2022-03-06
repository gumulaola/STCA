# 八皇后

n = 4


def solution(n):
    my_dict_col = {}
    my_dict_A = {}
    my_dict_B = {}

    path = []
    ans = []

    def get_valid(row):
        res = []
        for col in range(n):
            if col not in my_dict_col and (row - col) not in my_dict_A and (row + col) not in my_dict_B:
                res.append(col)
        return res

    def back(row):
        if row == n-1:
            cols = get_valid(row)
            if cols:
                path.append(cols[0])
                ans.append(path[:])
                path.pop()
            return

        cols = get_valid(row)
        for col in cols:
            path.append(col)
            my_dict_col[col] = True
            my_dict_A[row-col] = True
            my_dict_B[row+col] = True
            back(row+1)
            path.pop()
            my_dict_col.pop(col)
            my_dict_A.pop(row-col)
            my_dict_B.pop(row+col)

    back(0)
    print(ans)


solution(n)
