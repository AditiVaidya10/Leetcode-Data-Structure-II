class Solution:
    def partitionLabels(self, s):
        result, splitStart, SplitEnd = [], 0, 0
        while splitStart<len(s):
            currentPart, remainingPart = list({i:i for i in s[splitStart:SplitEnd+1]}), s[SplitEnd+1:][::-1]
            i = 0
            while i<len(currentPart):
                if currentPart[i] in remainingPart:
                    SplitEnd = len(s)-remainingPart.find(currentPart[i])-1
                    currentPart, remainingPart = list({i:i for i in s[splitStart:SplitEnd+1]}), s[SplitEnd+1:][::-1]
                i += 1
            result.append(len(s[splitStart:SplitEnd+1]))
            splitStart = SplitEnd = SplitEnd+1
        return result
