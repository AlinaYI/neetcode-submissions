class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # position/speed
        # curr time < prevTime, same fleet

        cars = sorted( zip(position, speed), reverse = True )
        stack = []
        # from the maxPosition

        for pos, sped in cars:
            currTime = (target - pos)/sped
            if not stack or currTime > stack[-1]:
                stack.append(currTime)
        return len(stack)