class Logger:
    
    def __init__(self):
        self.init_time = 0
        self.prev = {}
        self.curr = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if(timestamp >= self.init_time + 10):
            self.prev = self.curr.copy()
            self.curr.clear()
            self.init_time = timestamp
        if(self.curr.get(message) != None):
            return False
        if(self.prev.get(message) and self.prev[message] + 10 > timestamp):
            return False
        self.curr[message] = timestamp
        return True