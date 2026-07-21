class TimeMap:

    def __init__(self):
        # {name:[(1,mood), (1, mood)], name:[(1,mood)]}
        self.all = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.all[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        mood = self.all[key]

        left = 0
        right = len(mood)-1
        res = ""

        while left <= right:
            mid = left + (right-left)//2

            if mood[mid][0] == timestamp:
                return mood[mid][1]
            elif mood[mid][0] > timestamp:
                right = mid - 1
            else:
                res = mood[mid][1]
                left  = mid + 1
        return res