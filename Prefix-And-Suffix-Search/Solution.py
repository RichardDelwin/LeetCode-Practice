class WordFilter:

    def __init__(self, words):
        # print(words)
        self.words = words 
        self.prefix_trie = Trie()
        self.suffix_trie = Trie()
        
        for i, word in enumerate(words):
            self.prefix_trie.insert(word, i)
            self.suffix_trie.insert(word[::-1], i)

    def f(self, prefix, suffix):
        
        # print(prefix, suffix[::-1])
        pre_indices = self.prefix_trie.startsWith(prefix)
        suff_indices = self.suffix_trie.startsWith(suffix[::-1])
        # print(pre_indices, suff_indices)
        i, j = len(pre_indices)-1, len(suff_indices)-1
        
        while i>=0 and j>=0:
            
            if pre_indices[i] == suff_indices[j]:
                return pre_indices[i]
            
            elif pre_indices[i]>suff_indices[j]:
                i-=1
            
            else:
                j-=1
        
        return -1
    

class Trie:
    
    def __init__(self):
        
        self.index = []
        self.tree = {}

    def insert(self, word, index):
        
        root = self
        
        for char in word:
            
            if char not in root.tree:
                root.tree[char] = Trie()
            
            root = root.tree[char]
        
            root.index.append(index)
        
    def startsWith(self, word):
        
        root = self
        for char in word:
            
            if char not in root.tree:
                return []
            root = root.tree[char]
        
        return root.index




obj = WordFilter(["burnaby","apple", "ape", "applet"])
param_1 = obj.f("b","y")
print(param_1)


obj = WordFilter(["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"])
pre_suff= [["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]

for ps in pre_suff:
    pre, suff = ps

    param_1 = obj.f(pre, suff)
    print(param_1)
