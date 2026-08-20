class TimeMap:

    def __init__(self):
        # name: [timestamp, mood]
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        mood = self.hashmap[key]

        left, right = 0, len(mood) - 1
        res = ""
        while left <= right:
            mid = left + (right-left)//2

            if mood[mid][0] == timestamp:
                return mood[mid][1]
            elif mood[mid][0] > timestamp:
                right = mid - 1
            else:
                res = mood[mid][1]
                left = mid + 1
        return res
