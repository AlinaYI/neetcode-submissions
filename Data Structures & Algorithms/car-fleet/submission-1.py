class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        按照位置从前往后看

        当前车更早或同时到终点
        → 它会追上前车
        → 合并，不新增 fleet

        当前车更晚到终点
        → 它追不上
        → 新增 fleet
        '''
        
        ##position 越大，代表车越靠近终点
        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        for pos, sped in cars:
            time = (target-pos)/sped
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)