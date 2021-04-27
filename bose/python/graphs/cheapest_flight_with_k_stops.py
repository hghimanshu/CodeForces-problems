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


class FindPath:

    def __init__(self,graph):
        self.max_cost = float("inf")
        self.graph = graph
    
    def getCheapestPathWithinKStops(self,start,dst,k):

        # We don't need to mark the nodes as processed since we need to check for multiple paths

        queue = [(0,start,0)]
        heapify(queue)

        while queue:
            data = heappop(queue)

            node = data[1]
            cost = data[0]
            steps = data[2]

            if node==dst:
                self.max_cost = min(cost,self.max_cost)

            if node in self.graph:
                for adjNode in self.graph[node]:
                    if steps <=k and (self.graph[node][adjNode] + cost < self.max_cost):
                        heappush(queue,(self.graph[node][adjNode] + cost,adjNode,steps+1))
        if self.max_cost == float("inf"):
            return -1
        return self.max_cost

        

if __name__ == "__main__":
    g= Graph()
    edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    g.createGraph(edges)
    print(g.graph_dict)
    
    find = FindPath(g.graph_dict)
    print(find.getCheapestPathWithinKStops(src,dst,k))


