class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        last_seen={}
        longest=0
        for right in range(len(s)):
            char=s[right]
            if char in last_seen:
                left=max(left,last_seen[char]+1)
            last_seen[char]=right
            longest=max(longest,right-left+1)
        return longest
