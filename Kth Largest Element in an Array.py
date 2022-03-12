class Solution:
	def findKthLargest(self, nums, k):
		import heapq
		heapify(nums)
		return nlargest(k, nums)[-1]
