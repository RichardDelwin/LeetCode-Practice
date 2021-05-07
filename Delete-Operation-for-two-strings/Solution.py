class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        w1 = [""]
        w2 = [""]
        w1.extend(list(word1))
        w2.extend(list(word2))

        d = [[0]*len(w1) for _ in range(len(w2))]
        
        for c1 in range(len(w1)):
            d[0][c1] = c1
        for c2 in range(len(w2)):
            d[c2][0] = c2
        
        
        for c1 in range(1,len(w2)):
            for c2 in range(1,len(w1)):
                if w1[c2] != w2[c1]:
                    d[c1][c2] = min(d[c1-1][c2]+1, d[c1][c2-1]+1, d[c1-1][c2-1]+2)
                else:
                    d[c1][c2] = min(d[c1-1][c2]+1, d[c1][c2-1]+1, d[c1-1][c2-1])
        return d[-1][-1]



        
        
obj = Solution()
word1 = "sea"
word2 = "eat"
obj.minDistance(word1, word2)