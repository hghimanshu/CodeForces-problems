from heapq import heappop, heappush, heapify
class Graph:

    def __init__(self):
        self.graph_dict = {}

    def createGraph(self,edgeList,probList):
        for i in range(0,len(edgeList)):
            start = edgeList[i][0]
            end = edgeList[i][1]
            cost = probList[i]
            self.addEdge(start,end,cost)

            end = edgeList[i][0]
            start = edgeList[i][1]
            self.addEdge(start,end,cost)
        
    def addEdge(self,node,adj,cost):
        if node in self.graph_dict:
            self.graph_dict[node].update({adj:cost})
        else:
            self.graph_dict[node] = {adj:cost}

class Djiktras:
    def __init__(self,graph,n):
        self.graph = graph
        self.values = [0]*n
        self.parent = [-1]*n
        self.processed = [False]*n

    def getMinVertex(self):
        minVal = 0
        minIdx = 0
        for i,val in enumerate(self.values):
            if not self.processed[i]:
                if val > minVal:
                    minVal = val
                    minIdx = i
        return minIdx

    def getShortestPath(self,start,end):
        self.values[start]=1
        self.parent[start]= -1

        queue = [(-1, start)]
        heapify(queue)

        while queue:
            node = heappop(queue)[1]
            if self.processed[node]:
                continue

        # for i in range(0,len(self.values)-1):

            # node = self.getMinVertex()
            self.processed[node] = True

            for adjNode in self.graph[node]:
                if self.graph[node][adjNode]!=1 and not self.processed[adjNode] and self.values[node]!=0:
                    newCost = self.values[node]*self.graph[node][adjNode]
                    if newCost > self.values[adjNode]:
                        self.values[adjNode] = newCost
                        self.parent[adjNode] = node
                        heappush(queue, (-self.values[adjNode], adjNode))    

        return self.values[end]

class Solution:
    def maxProbability(self,n, edges,succProb,start,end):
            g = Graph()
            g.createGraph(edges,succProb)
            print(g.graph_dict)
            dik = Djiktras(g.graph_dict,n)
            if start not in g.graph_dict or end not in g.graph_dict:
                return 0
            maxProb = dik.getShortestPath(start,end)
            return maxProb
        
        # print(numOfReachableCities)

        # minCount = float('inf')
        # output = -1

        # for i,val in enumerate(numOfReachableCities):
        #     if val <= minCount:
        #         minCount = val
        #         if i > output:
        #             output = i
        # return output


            
if __name__ == "__main__":
    sol = Solution()
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.3]
    start = 1
    end = 2
    print(sol.maxProbability(n,edges,succProb,start,end))
    # distanceThreshold = 417
    # print(sol.findTheCity(n,edges,distanceThreshold))
        
