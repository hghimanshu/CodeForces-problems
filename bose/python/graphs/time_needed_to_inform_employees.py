class TimeNeeded:

    def __init__(self):
        self.graph ={}
        self.head=-1

    def createGraph(self,emp):
        for i in range(0,len(emp)):
            if i==self.head:
                continue
            if emp[i] not in self.graph:
                self.graph[emp[i]] = [i]
            else:
                self.graph[emp[i]].append(i)

    def numOfMinutes(self, headID, manager,informTime):
        self.head = headID
        self.createGraph(manager)
        print("Graph is :: {}".format(self.graph))
        
        self.maxTime = -1
        def dfs(graph,node):
            curr_time = -1
            if node in self.graph:
                for adjNode in graph[node]:
                    time = dfs(graph,adjNode)
                    self.maxTime = max(self.maxTime,time+informTime[node])
                    curr_time = max(curr_time,time)
                return curr_time+informTime[node]
            else:
                return informTime[node]
            # return time

        time = dfs(self.graph,self.head)
        return self.maxTime


if __name__ == "__main__":
    obj = TimeNeeded()
    # n = 15 
    # headID = 0 
    # manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
    # informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

    # n = 4
    # headID = 2
    # manager = [3,3,-1,2]
    # informTime = [0,0,162,914]

    n = 7
    headID = 6
    manager = [1,2,3,4,5,6,-1]
    informTime = [0,6,5,4,3,2,1]
    obj.numOfMinutes(headID, manager,informTime)
