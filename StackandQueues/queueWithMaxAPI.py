from collections import deque


class queue:
    def __init__(self):
        self.q = deque()
        self.max_q = deque()
    

    def enqueue(self, x):
        self.q.append(x)
        if len(self.max_q):
            for max_val in list(self.max_q):
                if x > max_val:
                    self.max_q.remove(max_val)
                    self.max_q.append(x)
        else:
            self.max_q.append(x)
    
    def deque(self):
        dequeued = self.q.popleft()
        if dequeued in self.max_q:
            self.max_q.remove(dequeued)
        
        if len(self.max_q) == 0:
            m = None
            for val in list(self.q):
                if m:
                    m = max(val, m)
                else:
                    m = val
            self.max_q.append(m)
    
    def maxElements(self):
        return self.max_q[0]


q = queue()
q.enqueue(10)
q.enqueue(50)
q.enqueue(20)
q.enqueue(10)
q.enqueue(0)
q.deque()
q.deque()
q.enqueue(16)
q.enqueue(89)
q.deque()
print(q.maxElements())
