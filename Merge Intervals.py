def merge(self, num: List[List[int]]) -> List[List[int]]:
        num.sort() # sort the list 
        l =[]
        for x in range(len(num)):
            if x == len(num)-1: 
                l.append(num[x])
                break
            if num[x][1]>=num[x+1][0]: 
                small = min(num[x][0],num[x+1][0]) 
                large = max(num[x][1],num[x+1][1]) 
                num[x+1][0], num[x+1][1]=small,large 
            else:
                l.append(num[x]) 
        return l
