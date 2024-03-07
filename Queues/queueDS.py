from collections import deque

class QueueDS:

    def __init__(self):
        self.buff = deque()
    
    def push(self,value):
        self.buff.appendleft(value)

    def pop(self):
        return self.buff.pop()
    
    def isEmpty(self):
        return len(self.buff)==0
    
    def get_length(self):
        return len(self.buff)
    
