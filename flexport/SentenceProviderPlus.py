import random


class SentenceProvider:
    def __init__(self, origin_sentence, m, k):
        self.origin_sentence = origin_sentence.split(" ")
        self.m = m
        self.k = k

        n = len(self.origin_sentence)

        right = 0
        start = []
        for _ in range(k):
            if right == n:
                right = 0

            start.append(self.origin_sentence[right])
            right += 1

        right -= 1

        self.char_map = {}
        for _ in range(n):
            cur = " ".join(start)
            nxt = None

            if right == n-1:
                nxt = self.origin_sentence[0]
            else:
                nxt = self.origin_sentence[right+1]

            if cur in self.char_map:
                self.char_map[cur].append(nxt)
            else:
                self.char_map[cur] = [nxt]

            start.pop(0)
            right += 1
            if right == n:
                right = 0
            start.append(self.origin_sentence[right])

    def next(self):
        keys_list = list(self.char_map.keys())
        start = random.choice(keys_list)
        window = start.split(" ")
        res = window[:]
        while len(res) < self.m:
            temp = " ".join(window)
            nxt = random.choice(self.char_map[temp])
            res.append(nxt)
            window.pop(0)
            window.append(nxt)
        return " ".join(res)


ins = SentenceProvider(
    "this is a sentence it is not a good one and it is also bad", 5, 2)
print(ins.next())
