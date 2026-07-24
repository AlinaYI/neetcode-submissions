class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        brute force
        尝试不同的牌作为开头，然后如果不行就backtrack
        exponential time

        sort，用最小的最为group开头，
        然后最小的必然是下一个group的开头，因为要incresing 1 的group
        在start -> start + groupSize 这些数字里面，频率不能小于这个start的频率
        因为要组成
        '''

        if len(hand)%groupSize != 0:
            return False

        hand.sort()
        count = Counter(hand)
        for start in hand:
            start_count = count[start]

            if start_count > 0:
                for card in range(start, start + groupSize):
                    if count[card] < start_count:
                        return False

                    count[card] -= start_count
        return True
