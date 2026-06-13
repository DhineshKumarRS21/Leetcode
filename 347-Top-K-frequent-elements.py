# sorting approach
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sorted_items = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result

  # Heap

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        max_heap = []
        for num, count in freq.items():
            heapq.heappush(max_heap, (-count, num))
        result = []
        for _ in range(k):
            count, num = heapq.heappop(max_heap)
            result.append(num)
        return result

  # Bucket sort
  
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        n = len(nums)
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        bucket=[[] for _ in range(n+1)]
        for num,count in dict.items():
            bucket[count].append(num)
        res=[]
        for i in range(n,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res
