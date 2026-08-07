class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted( zip(position, speed), reverse = True)

        stack = []
        for pos, sped in cars:
            time = (target-pos)/sped

            # 如果time小，或者 == 之前的，说明会更快的到达终点
            # 不会增加这个fleet，就不用更新
            # 如果大，就说明追不上，要更新fleet
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
