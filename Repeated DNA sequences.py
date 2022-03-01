class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dct = {}
        i = 0
        j = 10
        while (j<=len(s)):
            key = s[i:j]
            if key in dct:
                dct[key]+=1
            else: dct[key] = 1
            i+= 1
            j+= 1
        res=[]
        for k,v in dct.items():
            if v>1:
                res.append(k)
        return res
