class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        import heapq
        
        #We're going to be pushing values into our heap called distance, so we need to calculate using x ^ 2 + y ^ 2
        distance = []
        for x, y in points:
            dis = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(distance, (dis, [x, y]))
        
        #Return Array
        res = []
        
        #append to res k coordinates
        while k:
            dis, point = heapq.heappop(distance)
            res.append(point)
            k -= 1
        
        #return res
        return res
