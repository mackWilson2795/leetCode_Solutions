class RecentCounter:
    _ms = 3000
    
    def __init__(self):
        self.stack = []

    def ping(self, t: int) -> int:
        low_bound = t - self._ms
        self.stack.append(t)
        while(self.stack[0] < low_bound):
            self.stack = self.stack[1:]
        return len(self.stack)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)