class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums)):
            result_dict = dict()
            for j in range(i+1, len(nums)):
                values =- nums[i] - nums[j]
                if values in result_dict:
                    result.add(tuple(sorted([nums[i], nums[j], values])))
                else:
                    result_dict[nums[j]] = j
        return list(result)
