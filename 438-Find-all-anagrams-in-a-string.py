class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict_p={}
        for i in p:
            dict_p[i]=dict_p.get(i,0)+1
        if len(p)>len(s):
            return []
        dict_s={}
        for i in range(len(p)):
            dict_s[s[i]]=dict_s.get(s[i],0)+1
        res=[]
        if dict_p==dict_s:
            res.append(0)
        for i in range(len(p),len(s)):
            ch=s[i-len(p)]
            dict_s[ch] -= 1
            if dict_s[ch] == 0:
                dict_s.pop(ch)
            dict_s[s[i]]=dict_s.get(s[i],0)+1
            if dict_p==dict_s:
                res.append(i-len(p)+1)
        return res
