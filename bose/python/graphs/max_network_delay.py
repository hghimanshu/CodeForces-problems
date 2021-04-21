from heapq import heappop, heappush, heapify

class Graph:

    def __init__(self):
        self.graph_dict = {}

    def createGraph(self,edgeList):
        for i in range(0,len(edgeList)):
            start = edgeList[i][0]
            end = edgeList[i][1]
            cost = edgeList[i][2]
            self.addEdge(start,end,cost)

    def addEdge(self,node,adj,cost):
        if node in self.graph_dict:
            self.graph_dict[node].update({adj:cost})
        else:
            self.graph_dict[node] = {adj:cost}



class Djiktras:

    def __init__(self,graph,n):
        self.graph = graph
        self.values = {}
        self.processed = {}

    def getNetworkPath(self,start,n):
        for i in range(1,n+1):
            self.values[i] = float("inf")
        
        for i in range(1,n+1):
            self.processed[i] = False

        self.values[start] = 0
        queue = [(0,start)]

        heapify(queue)

        while queue:
            node = heappop(queue)[1]
            if self.processed[node]:
                continue
            self.processed[node]= True
            if node not in self.graph:
                continue
            for adjNode in self.graph[node]:
                if not self.processed[adjNode]:
                    newCost = self.values[node]+self.graph[node][adjNode]
                    if newCost < self.values[adjNode]:
                        self.values[adjNode] = newCost
                        heappush(queue,(self.values[adjNode],adjNode))

        max_delay = 0
        for k,v in self.values.items():
            if v==float('inf'):
                return -1
            if v>max_delay:
                max_delay = v
            
        return max_delay

if __name__ == "__main__":
    g = Graph()
    # times = [[2,1,1],[2,3,1],[3,4,1]]
    times = [[1,2,1]]
    n = 2
    k = 2
    g.createGraph(times)
    dik = Djiktras(g.graph_dict,n)
    print(dik.getNetworkPath(k,n))