class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq
        freq = Counter(nums)
        heap = [(freq[num], num) for num in list(freq.keys())[:k]]
        heapify(heap)
        for num in list(freq.keys())[k:]:
            heappushpop(heap, (freq[num], num))
        return [j for i,j in heap]
