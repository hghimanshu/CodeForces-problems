class Graph:


    graph_dict = []

    def addEdge(self,neighborList):
        self.graph_dict.append(neighborList)


class DetectPaths:

    def getPaths(self,graph):
        
        start = 0
        finalPostion = len(graph)-1
        paths = []

        def findPath(graph,index,curr_path):
            curr_path+=[index]
            if index == finalPostion:
                paths.append(curr_path)
                return curr_path
            for node in graph[index]:
                curr_path = findPath(graph,node,curr_path)
                curr_path = curr_path[0:-1]
            return curr_path

        findPath(graph,0,[])
        return paths

if __name__ == '__main__':
    g = Graph()
    # g.addEdge([1,2])
    # g.addEdge([3])
    # g.addEdge([3])
    # g.addEdge([])


    # g.addEdge([4,3,1])
    # g.addEdge([3,2,4])
    # g.addEdge([3])
    # g.addEdge([4])
    # g.addEdge([])

    edges = [[1,3],[2],[3],[]]
    for edge in edges:
        g.addEdge(edge)
   
    print(g.graph_dict)
    det = DetectPaths()
    print(det.getPaths(g.graph_dict))