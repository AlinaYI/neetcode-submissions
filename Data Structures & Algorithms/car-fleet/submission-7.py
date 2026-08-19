class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 这里就是要看能不能追上上一个，如果能追上就合并
        # 那这个的问题就是，对比time
        # postion/speed， 如果currTime < prevTime, 那就是会追上
        cars = sorted( zip(position, speed), reverse=True)
        stack = []
        for pos, sped in cars:
            time = (target-pos)/sped
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)