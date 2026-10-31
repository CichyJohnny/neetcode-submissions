class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((timestamp, value))
        else:
            self.timemap[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        val = self.timemap.get(key, None)
        if not val: return ""

        l = 0
        p = len(val) - 1

        maxx = None
        while l <= p:
            i = (l + p) // 2

            if val[i][0] <= timestamp:
                l = i + 1
                if not maxx or maxx[0] < val[i][0]:
                    maxx = (i, val[i][0])
            else:
                p = i - 1
        
        if maxx:
            return val[maxx[0]][1]
        else:
            return ""
