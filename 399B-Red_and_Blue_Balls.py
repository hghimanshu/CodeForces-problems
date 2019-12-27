class myStack:
    def __init__(self):
        self.container = [] 
        self.count = 0

    def push(self, pos, item):
        self.container.insert(pos, item) 

    def pop(self):
        return self.container.pop(0)

    def replace(self, ball, count):
        self.container.remove(ball)
        self.container.insert(0, 'R')
        self.count +=1
        return self.count
    
    def show(self):
        return self.container 
    

def pushSomeBalls(total_size, remain_size):
    remain_blue_balls = total_size - remain_size
    for i in range(remain_blue_balls):
        s.push(0, 'B')

def operations(remain_balls, n):
    operation_count = 0
    while remain_balls.count('B') != 0:
        if remain_balls[0] == 'R':
            s.pop()
        elif remain_balls[0] == 'B':
            operation_count = s.replace(remain_balls[0], operation_count)
            pushSomeBalls(n, len(remain_balls))
    return operation_count

def insertingBalls(balls):
    for i, ball in enumerate(balls):
        s.push(i, ball)
    
if __name__ == "__main__":
    # n = int(input())
    # balls = str(input())
    n = 30
    balls = 'RRBBBBBBBBBBBBBBBBBBBBBBBBBBBB'
    s = myStack()
    insertingBalls(balls)
    ans = operations(s.show(), len(balls))
    print(ans)