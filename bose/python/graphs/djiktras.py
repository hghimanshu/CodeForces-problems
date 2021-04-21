    class Graph:

    def __init__(self):
        self.graph_dict = {}

    def createGraph(self,edgeList):
        for nodeList in edgeList:
            start = nodeList[0]
            end = nodeList[1]
            cost = nodeList[2]
            self.addEdge(start,end,cost)

            start = nodeList[1]
            end = nodeList[0]
            self.addEdge(start,end,cost)
    
        
    def addEdge(self,node,adj,cost):
        if node in self.graph_dict:
            self.graph_dict[node].update({adj:cost})
        else:
            self.graph_dict[node] = {adj:cost}

class Djiktras:

    def __init__(self,graph):
        self.graph = graph
        self.values = [float('inf')]*len(self.graph.keys())
        self.parent = [-1]*len(self.graph.keys())
        self.processed = [False]*len(self.graph.keys())

    def getMinVertex(self):
        minVal = float('inf')
        minIdx = 0
        for i,val in enumerate(self.values):
            if not self.processed[i]:
                if val < minVal:
                    minVal = val
                    minIdx = i
        return minIdx

    def getShortestPath(self,start):
        self.values[start]=0
        self.parent[start]= -1

        for i in range(0,len(self.values)-1):

            node = self.getMinVertex()
            self.processed[node] = True

            for adjNode in self.graph[node]:
                if self.graph[node][adjNode]!=0 and adjNode and not self.processed[adjNode] and self.values[node]!=float('inf'):
                    newCost = self.values[node] + self.graph[node][adjNode]
                    if newCost < self.values[adjNode]:
                        self.values[adjNode] = newCost
                        self.parent[adjNode] = node    

if __name__ == "__main__":
    edgeList = [
        [0,1,1],[1,4,7],[4,5,7],[3,5,6],[2,3,3],[0,2,4],[1,3,2],[2,1,4],[2,4,5]
    ]
    g = Graph()
    g.createGraph(edgeList)
    print(g.graph_dict)
    dik = Djiktras(g.graph_dict)
    dik.getShortestPath(0)