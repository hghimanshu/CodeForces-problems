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
    
    def find_path_dfs(self,start,end,path=[]): #DFS
        path+=[start]

        if start == end:
            return path

        for node in self.graph_dict[start]:
            if node not in path:
                newPath = self.find_path_dfs(node,end,path)
                if newPath:
                    return newPath
                return None

    def find_path_bfs(self,s): 
        visited = {}
        for i in self.graph_dict:
            visited[i] = False
        
        queue = []
        queue.append(s)
        visited[s] = True
        while len(queue)!=0:
            s = queue.pop(0)
            for node in self.graph_dict[s]:
                if visited[node]!=True: #not visited
                    visited[node] = True
                    queue.append(node)
            print(s)

    

    


    

if __name__ == "__main__":

    g= Graph()
    g.addEdge('1', '2')
    g.addEdge('1', '3')
    g.addEdge('2', '3')
    g.addEdge('2', '1')
    g.addEdge('3', '1')
    g.addEdge('3', '2')
    g.addEdge('3', '4')
    g.addEdge('4', '3')
    g.show_edges()
    print(g.find_path_dfs('4','1'))
    print(g.find_path_bfs('1'))