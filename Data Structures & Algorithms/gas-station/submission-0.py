class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        这道题就是从哪里开始能travel circuit
        '''

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i]
            total -= cost[i]

            if total < 0:
                start = i + 1
                total = 0
        return start