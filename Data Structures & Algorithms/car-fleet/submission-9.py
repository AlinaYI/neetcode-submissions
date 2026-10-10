class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 这里就是要算 time（target-position）/speed
        # 如果time 大就append
        cars = sorted( zip(position, speed), reverse=True )
        stack = []
        for i in range(len(cars)):
            time = (target-cars[i][0])/cars[i][1]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)