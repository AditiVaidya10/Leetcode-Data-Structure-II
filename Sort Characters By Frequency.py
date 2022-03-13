class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for character in s:
            if character in dic:
                dic[character] += 1
            else:
                dic[character] = 1
                
        lis1 = []
        lis2 = []
        for character in dic:
            lis1.append(character)
            lis2.append(dic[character])
    
        st = ""
        while len(lis1) and len(lis2):
            for i in range(max(lis2)):
                st += lis1[lis2.index(max(lis2))]
            lis1.pop(lis2.index(max(lis2)))
            lis2.pop(lis2.index(max(lis2)))
            
        return st
