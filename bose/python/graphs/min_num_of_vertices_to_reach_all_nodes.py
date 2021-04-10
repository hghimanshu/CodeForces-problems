

class MinVertices:

    # def __init__(self):
    #     self.minVertices = []
    #     self.graph ={}
    #     self.visited = {}

    # def createGraph(self,edgeList):
    #     for edge in edgeList:
    #         if edge[0] not in self.graph:
    #             self.graph[edge[0]] = [edge[1]]
    #         else:
    #             self.graph[edge[0]].append(edge[1])
        


    # def dfs(self,node):
    #     if node in self.visited:
    #         return
    #     self.visited[node] = True
    #     if node in self.graph:
    #         for adjNode in self.graph[node]:
    #             self.dfs(adjNode)


    def findSmallestSetOfVertices(self, n, edges):
        # self.createGraph(edges)
        # print("Graph created from edge list is :: {}".format(self.graph))

        visited = {}
        
        minVertices = []

        for i in range(0,len(edges)):
            visited[edges[i][1]] = True

        print(visited)

        for i in range(0,len(edges)):
            if edges[i][0] not in visited:
                minVertices.append(edges[i][0])
       

        return list(set(minVertices))



if __name__ == "__main__":
    n= 6
    # edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    edges= [[0,1],[2,1],[3,1],[1,4],[2,4]]
    obj = MinVertices()
    print(obj.findSmallestSetOfVertices(n,edges))