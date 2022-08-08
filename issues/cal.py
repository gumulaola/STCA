from __future__ import barry_as_FLUFL


class Solution:
    def calculate(self, s):
        s.replace(" ", "")
        n = len(s)

        my_dict = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
        }

        nums = []
        ops = []

        i = 0
        while i < n:
            # "(" ")"
            if s[i] == "(":
                ops.append("(")
            elif s[i] == ")":
                while ops[-1] != "(":
                    self.cal(nums, ops)
                ops.pop()

            # +-*/ num
            else:
                # num
                if s[i].isdigit():
                    cur_num = s[i]
                    while i+1 < n and s[i+1].isdigit():
                        cur_num += s[i+1]
                        i += 1
                    cur_num = int(cur_num)
                    nums.append(cur_num)

                # +-*/
                else:
                    while ops and ops[-1] != "(":
                        prev_ops = ops[-1]
                        if my_dict[prev_ops] >= my_dict[s[i]]:
                            self.cal(nums, ops)
                        else:
                            break
                    ops.append(s[i])
            i += 1

        while ops:
            self.cal(nums, ops)

        return nums.pop()

    """
    [ "(" , "+" ]
    ["3", "1"]
    """

    def cal(self, nums, ops):
        cur_ops = ops.pop()
        print(cur_ops)

        b = nums.pop()
        a = nums.pop()

        ans = 0
        if cur_ops == "+":
            ans = a + b
        elif cur_ops == "-":
            ans = a - b
        elif cur_ops == "*":
            ans = a * b
        elif cur_ops == "/":
            ans = a // b

        nums.append(ans)
        print(nums)
        print(ops)
        print("******")


# Test
test_ins = Solution()
input = "3+4-(4*5+10)/2"
res = test_ins.calculate(input)
print(res)
