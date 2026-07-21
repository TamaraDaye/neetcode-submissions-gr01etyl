class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False 


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def add(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c] 
        curr.is_word = True


    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False 
            curr = curr.children[c]

        return True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()

        for word in dictionary:
            trie.add(word)

        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)

            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break

                curr = curr.children[s[j]]
                if curr.is_word:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res

        return dfs(0)


        


