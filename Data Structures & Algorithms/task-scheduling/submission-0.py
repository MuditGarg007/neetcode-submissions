class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        clock = 0

        pq = []
        queue = deque()

        freq = Counter(tasks)

        for f in freq:
            heapq.heappush(pq, -freq[f])


        while pq or queue:
            while queue and queue[0][1] <= clock:
                heapq.heappush(pq, -queue.popleft()[0])

            if not pq:
                tsk, time = queue.popleft()
                clock = time
                heapq.heappush(pq, -tsk)
                continue
            task = -heapq.heappop(pq)
            task -=1

            if task>0:
                queue.append((task, clock+n+1))



            clock+=1

        return clock
            
            

        