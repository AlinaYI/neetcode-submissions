class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # time = position/speed
        cars = sorted( zip(position, speed), reverse = True )
        stack = []
        for pos, sped in cars:
            currTime = (target -pos)/sped

            # 如果currTime 比之前小，那说明追的上，car fleets不变
            if not stack or currTime > stack[-1]:
                stack.append(currTime)
        return len(stack)
            