class Solution:
    def countPrimes(self, n: int) -> int:
        
        
        l = [True for i in range(n)]
        
        
        if n in [0,1,2]:
            return 0
        
        if n==3:
            return 1
        
        pr = 2

        while pr*pr<n:
            if l[pr]:

                for i in range(pr*2, n, pr):
                    l[i]=False
            
            pr+=1

        count = 0
        for i in l:
            count+= 1 if i else 0    
        
        return count -2

obj = Solution()
ans = obj.countPrimes(10)
print(ans)