class TimeMap:
    """
    10^7 timestamps so looks too big. Binary search maybe
    For a key, find boundary condition: largest t lesser than input

    To initialize: a dict of key as key and tuple(time, value) as value
    To set: set sorted by time
    To get: Binary search over tuple[0]
    """
    def __init__(self):
        self.mapper = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapper:
            self.mapper[key].append((timestamp, value))
        else:
            self.mapper[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        res = ""; times = self.mapper.get(key, [])
        l = 0; r = len(times)-1

        while l <= r:
            m = l + (r-l)//2

            if times[m][0] <= timestamp:
                l = m+1
                res = times[m][1]
            else:
                r = m-1
        
        return res



        
