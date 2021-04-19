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
        self.values = [float('inf')]*len(self.graph)
        self.parent = [-1]*len(self.graph)
        self.processed = [False]*len(self.graph)

    def getMinVertex(self):
        minVal = float('inf')
        minIdx = 0
        for i,val in enumerate(self.values):
            if not self.processed[i]:
                if val < minVal:
                    minVal = val
                    minIdx = i
        return minIdx

    def getShortestPath(self,start,threshold):
        self.values[start]=0
        self.parent[start]= -1

        for i in range(0,len(self.values)-1):

            node = self.getMinVertex()
            self.processed[node] = True

            for adjNode in self.graph[node]:
                if self.graph[node][adjNode]!=0 and not self.processed[adjNode] and self.values[node]!=float('inf'):
                    newCost = self.values[node] + self.graph[node][adjNode]
                    if newCost < self.values[adjNode]:
                        self.values[adjNode] = newCost
                        self.parent[adjNode] = node    

        validCount = 0
        for i,val in enumerate(self.values):
            if i!=start:
                if val<=threshold:
                    validCount+=1
        return validCount

class Solution:
    def findTheCity(self,n, edges,distanceThreshold):
        g = Graph()
        g.createGraph(edges)
        numOfReachableCities = [0]*n
        for i in range(0,n):
            if i not in g.graph_dict:
                continue
            dik = Djiktras(g.graph_dict)
            numOfReachableCities[i] = dik.getShortestPath(i,distanceThreshold)
        
        print(numOfReachableCities)

        minCount = float('inf')
        output = -1

        for i,val in enumerate(numOfReachableCities):
            if val <= minCount:
                minCount = val
                if i > output:
                    output = i
        return output


            
if __name__ == "__main__":
    sol = Solution()
    n = 6
    edges = [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]]
    distanceThreshold = 417
    print(sol.findTheCity(n,edges,distanceThreshold))
        
