class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self._k = k

        for num in nums:
            heapq.heappush(self.pq, num)
            if len(self.pq)>k:
                heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)

        while len(self.pq) > self._k:
            heapq.heappop(self.pq)
        return self.pq[0]
        
