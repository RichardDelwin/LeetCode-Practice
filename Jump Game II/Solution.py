class Solution:
    
    def jump(self, nums: List[int]) -> int:
        
        if nums[0] == 0 or len(nums) == 1:
            return 0
        jumps = 1
        longest_stride = nums[0]
        current_end = nums[0]
        
        for i in range(1, len(nums)-1):
            
            longest_stride = max(longest_stride, nums[i]+i)
            
            if i == current_end:    
                jumps += 1
                current_end = longest_stride
            
        return jumps
            