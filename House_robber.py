class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n <= 2:
            return max(nums)
        lt=[0]*n
        lt[0]=nums[0]
        lt[1]=max(nums[:2])
        for i in range(2,n):
            lt[i]=max(nums[i]+lt[i-2],lt[i-1])
        return lt[-1]
