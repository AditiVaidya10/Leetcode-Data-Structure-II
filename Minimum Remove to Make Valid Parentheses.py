class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        brack = []
        sg = set()
        for i in range(len(s)):
            if s[i] != ")" and s[i] != "(":
                stack.append(s[i])
            else:
                if brack and brack[-1][0] == "(" and s[i] == ")":
                    brack.pop()
                else:
                    brack.append((s[i],i))
        
        ans = ""        
        for res in brack:
            sg.add(res[1])
        for i in range(len(s)):
            if i not in sg:
                ans+=s[i]
        print(ans)
        
        return ans
                
