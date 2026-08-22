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
        '''
        getNewsFeed:
        O(F log F + 10 log F)
        ≈ O(F log F)
        '''
        
        allUsers = self.followed[userId]
        allUsers.add(userId)
        
        # 要从最大的 ---> 最小的
        # 可以存一个maxHeap，然后每次都把最大的先拿出来存到res里面
        maxHeap = []
        res = []
        for user in allUsers:
            if self.tweet[user]:
                idx = len(self.tweet[user])-1
                time, tweetId = self.tweet[user][idx]

                heapq.heappush(maxHeap, (-time, tweetId, user, idx))

        while maxHeap and len(res) < 10:
            _, tweetId, user, idx = heapq.heappop(maxHeap)
            res.append(tweetId)

            if idx > 0:
                idx -= 1
                time, tweetId = self.tweet[user][idx]
                heapq.heappush(maxHeap, (-time, tweetId, user, idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].discard(followeeId)
