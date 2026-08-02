class Twitter:

    def __init__(self):
        self.friend = defaultdict(set)
        self.post = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.post[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        
        users = self.friend[userId]
        users.add(userId)
        maxHeap = []
        res = []

        for user in users:
            for time, tweetId in self.post[user]:
                heapq.heappush(maxHeap, (-time, tweetId))
        
        while maxHeap and len(res) < 10:
            time, tweetId = heapq.heappop(maxHeap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.friend[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.friend[followerId].discard(followeeId)
