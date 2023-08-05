class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
        self.failure_link = None
        self.output_link = []

class AhoCorasick:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True

    def build_failure_links(self):
        queue = []
        for child in self.root.children:
            if child:
                child.failure_link = self.root
                queue.append(child)
        while queue:
            current = queue.pop(0)
            for i in range(26):
                if current.children[i]:
                    child = current.children[i]
                    queue.append(child)
                    failure_link = current.failure_link
                    while failure_link and not failure_link.children[i]:
                        failure_link = failure_link.failure_link
                    child.failure_link = failure_link.children[i] if failure_link else self.root
                    child.output_link.extend(child.failure_link.output_link)
                    if child.is_end_of_word:
                        child.output_link.append(child)

    def search(self, text):
        result = []
        current = self.root
        for char in text:
            index = ord(char) - ord('a')
            while current != self.root and not current.children[index]:
                current = current.failure_link
            if current.children[index]:
                current = current.children[index]
            for node in current.output_link:
                result.append(node)
        return result
