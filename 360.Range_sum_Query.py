class NumArray:

    def __init__(self, nums: List[int]):
        self.lt=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.lt[i+1]=nums[i]+self.lt[i]


    def sumRange(self, left: int, right: int) -> int:
        return (self.lt[right+1]-self.lt[left])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
