import heapq


class Word:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.val > self.val


nums = []

heapq.heappush(nums, Word("hello", -0))
heapq.heappush(nums, Word("world", -10))
heapq.heappush(nums, Word("happy", -20))

print(heapq.heappop(nums).val)

print(Word("hello", -0) > Word("world", -10))
