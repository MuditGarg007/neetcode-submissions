class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        pq = []
        
        for point in points:
            x = point[0]
            y = point[1]
            heapq.heappush(pq, (x**2 + y**2, x, y))

        res = []
        for i in range(k):
            _, x, y = heapq.heappop(pq)
            res.append([x,y])

        return res



