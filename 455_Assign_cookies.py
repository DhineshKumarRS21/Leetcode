class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c,k=0,0
        count=0
        while(k<len(s) and c<len(g)):
            if g[c]<=s[k]:
                c+=1
                count+=1
                k+=1
            else:
                k+=1
        return count
