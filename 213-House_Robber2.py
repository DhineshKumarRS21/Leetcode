class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n <= 2: 
            return max(nums)
        lt=[0]*n
        lt[0]=nums[0]
        lt[1]=max(nums[:2])
        flag=False
        for i in range(2,n-1):
            lt[i]=max(nums[i]+lt[i-2],lt[i-1])
        lt[-1]=lt[-2]
        lt1=[0]*n
        lt1[0]=0
        lt1[1]=nums[1]
        for i in range(2,n):
            lt1[i]=max(nums[i]+lt1[i-2],lt1[i-1])
        return max(lt[-1],lt1[-1])
