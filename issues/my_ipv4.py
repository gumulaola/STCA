'''
给定任意数字字符串 返回能构成的 ipv4 地址

ipv4 pattern:
    4 个整数
    0 ~ 255
    不能含有前导 0 for example 0 ✅ 012 ❌
'''

input = "25525511135"
res = []
path = []


def valid(s):
    if s[0] == "0" and s != "0":
        return False
    s = int(s)
    if s >= 0 and s <= 255:
        return True
    else:
        return False


def back(start, point):
    if len(input[start:]) < 4-point or len(input[start:]) > (4-point)*3:
        return

    if point == 3:
        if valid(input[start:]):
            path.append(input[start:])
            # print("append")
            # print(path)

            res.append(".".join(path))

            path.pop()
            # print("pop")
            # print(path)
        return

    for i in range(1, 4):
        if valid(input[start:start+i]):
            path.append(input[start:start+i])
            # print("append")
            # print(path)

            back(start + i, point+1)

            path.pop()
            # print("pop")
            # print(path)


back(0, 0)
print(res)
