from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=deque()
        n=len(nums)
        arr=[-1]*n
        for i in range(2*n):
            ind=i%n
            while stack and nums[stack[-1]]<nums[ind]:
                index=stack.pop()
                arr[index]=nums[ind]
            if i < n:
                stack.append(ind)

        return arr
