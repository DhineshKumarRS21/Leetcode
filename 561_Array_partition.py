class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        tot=0
        for i in range(0,len(nums),2):
            tot+=nums[i]
        return tot
