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

class DetectAllPaths:

    def getPaths(self,graph,start,end):

        paths = []

        processed = [False]*len(graph)

        


if __name__ == "__main__":
    edgeList = [
        [1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]
    ]
    g = Graph()
    g.createGraph(edgeList)
    print(g.graph_dict)