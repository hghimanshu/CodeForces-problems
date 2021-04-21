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
        self.values = {}
        self.processed = {}
        for i in range(1,n+1):
            self.values[i] = float("inf")
        self.parent = [-1]*n
        for i in range(1,n+1):
            self.processed[i] = False

    def getShortestPath(self,n):
        self.values[n]=0

        queue = [(0,n)]
        heapify(queue)

        
        while queue:
            node = heappop(queue)[1]
            if self.processed[node]:
                continue

            self.processed[node] = True

            for adjNode in self.graph[node]:
                if not self.processed[adjNode]:
                    newCost = self.values[node]+self.graph[node][adjNode]
                    if newCost < self.values[adjNode]:
                        self.values[adjNode] = newCost
                        self.parent[adjNode] = node
                        heappush(queue, (self.values[adjNode], adjNode))    

        print(self.values)

class Solution:
    def maxProbability(self,n, edges):
            g = Graph()
            g.createGraph(edges)
            print(g.graph_dict)
            dik = Djiktras(g.graph_dict,n)
            # if start not in g.graph_dict or end not in g.graph_dict:
            #     return 0
            dik.getShortestPath(n)
            # return maxProb

            
if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
    print(sol.maxProbability(n,edges))

        
