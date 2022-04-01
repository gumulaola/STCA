# 实现前缀树

class Trie:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

    def insert(self, word):
        cur = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not cur.children[ch]:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.is_end = True

    def search_prefix(self, prefix):
        cur = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not cur.children[ch]:
                return False
            else:
                cur = cur.children[ch]
        return cur

    def search(self, word):
        res = self.search_prefix(word)
        return res is not None and res.is_end

    def startsWith(self, prefix):
        res = self.search_prefix(prefix)
        return res is not None
