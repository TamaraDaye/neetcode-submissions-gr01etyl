class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.is_word = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)

        ans = ""

        def dfs(i, node):
            nonlocal ans
            for c in node.children:
                for word in strs:
                    if i >= len(word):
                        return False
                    if word[i] != c:
                        return False
                ans += c

                if not dfs(i + 1, node.children[c]):
                    return False


        dfs(0, trie.root)

        return ans if ans else ""





                
            