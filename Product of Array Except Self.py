class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, L, R = len(nums), 1, 1
        p = [1] + [(L := L * nums[i]) for i in range(n - 1)]
        for i in range(1, n):
            p[-(i + 1)] *= (R := R * nums[-i])
        return p
