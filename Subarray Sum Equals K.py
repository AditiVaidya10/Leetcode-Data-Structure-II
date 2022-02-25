class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic, sm, count = defaultdict(int),0,0
        for i in nums:
            sm += i
            count += (sm == k) + dic[sm - k]
            dic[sm] += 1
        return count
