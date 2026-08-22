class Twitter:

    def __init__(self):
        # user1:[(timestamp, tweet)]
        self.tweet = defaultdict(list)
        # user1: [user1 followed users]
        self.followed = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append( (self.timestamp, tweetId) )
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        allUsers = self.followed[userId]
        allUsers.add(userId)
        
        # 要从最大的 ---> 最小的
        # 可以存一个maxHeap，然后每次都把最大的先拿出来存到res里面
        maxHeap = []
        res = []
        for user in allUsers:
            for time, tw in self.tweet[user]:
                heapq.heappush(maxHeap, (-time, tw))
        
        while maxHeap and len(res) < 10:
            _, tw = heapq.heappop(maxHeap)
            res.append(tw)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].discard(followeeId)
