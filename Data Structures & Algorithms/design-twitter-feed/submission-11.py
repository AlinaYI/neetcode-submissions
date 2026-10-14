class Twitter:

    def __init__(self):
        # {userId: [(timestamp, tweetId),(timestamp, tweetId)]}
        self.posts = defaultdict(list)
        # {userId:[followeeId]}
        self.relations = defaultdict(set)
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append( (self.timeStamp, tweetId) )
        self.timeStamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        allUsers = self.relations[userId]
        allUsers.add(userId)
        
        # 只存每个user最新的一条tweet
        maxHeap = []
        for user in allUsers:
            if self.posts[user]:
                idx = len(self.posts[user])-1
                timeStamp, tweetId = self.posts[user][idx]
                heapq.heappush(maxHeap, (-timeStamp, tweetId, user, idx))
        
        res = []
        while maxHeap and len(res) < 10:
            _, tweetId, user, idx = heapq.heappop(maxHeap)
            res.append(tweetId)

            if idx > 0:
                idx -= 1
                timeStamp, tweetId = self.posts[user][idx]
                heapq.heappush(maxHeap, (-timeStamp, tweetId, user, idx))
        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.relations[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.relations[followerId].discard(followeeId)
