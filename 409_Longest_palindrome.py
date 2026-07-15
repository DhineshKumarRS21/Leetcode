class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        flag=0
        count=0
        for i in freq.keys():
            if freq[i]%2!=0:
                count+=freq[i]-1
            else:
                count+=freq[i]
                continue
            if flag==0:
                flag=1
                count+=1
        return count
