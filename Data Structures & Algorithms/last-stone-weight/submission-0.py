class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []

        for stone in stones:
            heapq.heappush(pq, -stone)

        while len(pq)>1:
            x = -heapq.heappop(pq)
            y = -heapq.heappop(pq)
            
            if x>y:
                x = x-y
                heapq.heappush(pq,-x)
        

        if len(pq)==0:
            return 0
        return -pq[0]
