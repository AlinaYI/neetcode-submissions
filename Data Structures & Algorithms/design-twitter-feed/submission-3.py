class Twitter:

    def __init__(self):
        # follower: [ follweedId]
        self.friends = defaultdict(set)
        # userId:[tweetId]
        self.tweet = defaultdict(list)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append( (self.time, tweetId) )
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.friends[userId]
        users.add(userId)
        maxHeap = []

        for user in users:
            for t in self.tweet[user]:
                time, tweetId = t
                heapq.heappush(maxHeap, (-time, tweetId) )
        
        res = []
        while maxHeap and len(res) < 10:
            time, tweetId = heapq.heappop(maxHeap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.friends[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.friends[followerId].discard(followeeId)
