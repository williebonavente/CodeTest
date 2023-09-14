class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.start = None
        self.end = None

class SuffixTree:
    def __init__(self, string):
        self.root = SuffixTreeNode()
        self.string = string
        self.build_suffix_tree()

    def build_suffix_tree(self):
        n = len(self.string)
        for i in range(n):
            suffix = self.string[i:]
            current = self.root
            for char in suffix:
                if char not in current.children:
                    current.children[char] = SuffixTreeNode()
                current = current.children[char]
            current.start = i
            current.end = n - 1

    def search(self, pattern):
        current = self.root
        for char in pattern:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
