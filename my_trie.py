class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def searchPrefix(self, prefix):
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def search(self, word):
        prefix = self.searchPrefix(word)
        return prefix is not None and prefix.isEnd == True

    def startsWith(self, prefix):
        prefix = self.searchPrefix(prefix)
        return prefix is not None
