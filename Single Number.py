class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = result ^ i
        return result
        
