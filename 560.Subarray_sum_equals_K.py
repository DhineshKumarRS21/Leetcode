class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sums = {0: 1}
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            target = current_sum - k
            if target in prefix_sums:
                count += prefix_sums[target]  
            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1  
        return count
