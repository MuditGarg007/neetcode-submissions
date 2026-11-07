class Twitter:

    class Tweet:
        def __init__(self, id, time):
            self.id = id
            self.time = time
            self.next = None

        def __lt__(self, other):
            return self.time>other.time

    class User:
        def __init__(self):
            self.tweets = None
            self.followings = set()

    def __init__(self):
        self.users = {}
        self.clock = 0

    def createUser(self, userId):
        newUser = self.User()
        self.users[userId] = newUser

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.users:
            self.createUser(userId)
        tweet = self.Tweet(tweetId, self.clock)
        tweet.next = self.users[userId].tweets
        self.users[userId].tweets = tweet

        self.clock+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if not userId in self.users:
            self.createUser(userId)
            return []
        pq = []
        followings = self.users[userId].followings | {userId}
        feed = []
        ptrs = [self.users[following].tweets for following in followings]

        for ptr in ptrs:
            if ptr is not None:
                heapq.heappush(pq, (-ptr.time, ptr))

        while len(feed) < 10 and pq:
            _, ptr = heapq.heappop(pq)
            feed.append(ptr.id)
            ptr = ptr.next
            if ptr is not None:
                heapq.heappush(pq, (-ptr.time, ptr))

        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            self.createUser(followerId)
        if not followeeId in self.users:
            self.createUser(followeeId)

        self.users[followerId].followings.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users or not followeeId in self.users or followeeId not in self.users[followerId].followings:
            return

        self.users[followerId].followings.remove(followeeId)
        
