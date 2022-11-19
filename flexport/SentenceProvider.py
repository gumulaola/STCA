import random


class SentenceProvider:
    def __init__(self, origin_sentence, m):
        self.origin_sentence = origin_sentence.split(" ")
        n = len(self.origin_sentence)
        self.char_map = {}
        self.m = m

        for i in range(n):
            cur = None
            nxt = None

            if i != n-1:
                cur = self.origin_sentence[i]
                nxt = self.origin_sentence[i+1]
            else:
                cur = self.origin_sentence[n-1]
                nxt = self.origin_sentence[0]

            if cur in self.char_map:
                self.char_map[cur].append(nxt)
            else:
                self.char_map[cur] = [nxt]

    def next(self):
        res = [random.choice(self.origin_sentence)]
        for _ in range(self.m-1):
            res.append(random.choice(self.char_map[res[-1]]))
        return " ".join(res)


ins = SentenceProvider(
    "this is a sentence it is not a good one and it is also bad", 5)

for _ in range(10):
    print(ins.next())
