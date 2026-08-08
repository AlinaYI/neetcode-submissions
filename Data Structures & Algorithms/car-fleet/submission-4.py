class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 从离得近的开始算, 如果需要的time小于前面的，就可以合并，
        # 要不然就是新的car fleet
        # time = posotion/speed
        cars = sorted( zip(position, speed), reverse= True)
        stack = []

        for pos, sped in cars:
            time = (target - pos) / sped
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)