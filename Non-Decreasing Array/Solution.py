class Solution:
    def checkPossibility(self, nums):
        
        count = 0
        for i in range(1,len(nums)):
            
            if nums[i]<nums[i-1]:
                                
                if i == 1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                    count+=1
                
                else:
                    nums[i] = nums[i-1]
                    count+=1
                
                if count > 1:
                    break
        
        return count == 1 or count == 0


obj = Solution()
nums = [1,4,1,2]
res = obj.checkPossibility(nums)
print(res)