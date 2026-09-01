class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.followed = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        allUser = self.followed[userId]
        allUser.add(userId)
        maxHeap = []
        res = []
        # 所有的user先取最新的tweet
        for user in allUser:
            if self.tweet[user]:
                tweetIdx = len(self.tweet[user])-1
                timestamp, tweetId = self.tweet[user][-1]
                heapq.heappush(maxHeap, (-timestamp, tweetId, user, tweetIdx))

        while maxHeap and len(res) < 10:
            timestamp, tweetId, user, tweetIdx = heapq.heappop(maxHeap)
            res.append(tweetId)

            if tweetIdx-1 >= 0:
                timestamp, tweetId = self.tweet[user][tweetIdx-1]
                heapq.heappush(maxHeap, (-timestamp, tweetId, user, tweetIdx-1))
        return res
        
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].discard(followeeId)
