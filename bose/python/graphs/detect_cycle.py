class Graph:

    graph_dict = {}

    def addEdge(self,node,neighbor):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbor]
        else:
            self.graph_dict[node].append(neighbor)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbor in self.graph_dict[node]:
                print("( "+node+","+neighbor+")")


    def checkIfCycleExists(self,start):

        visited = [start]

        def check(curr):
            for node in self.graph_dict[curr]:
                if node not in visited:
                    visited.append(node)
                    if node==curr:
                        return True
                    cyclePresent = check(node)
                    if cyclePresent:
                        return True
            return False
        
        print(check(start))

if __name__ == "__main__":

    g= Graph()
    g.addEdge('1', '2')
    g.addEdge('1', '3')
    g.addEdge('2', '3')
    g.addEdge('2', '2')
    g.addEdge('3', '1')
    # g.addEdge('3', '1')
    # g.addEdge('3', '2')
    # g.addEdge('3', '4')
    # g.addEdge('4', '3')
    g.show_edges()
    g.checkIfCycleExists("1")