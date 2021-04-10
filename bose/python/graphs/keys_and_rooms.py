class keysAndRooms:

    visited ={}

    def canVisitAllRooms(self, rooms):
        for i in range(0,len(rooms)):
            self.visited[i] = False
        self.visited[0]=True
        self.dfs(rooms,0)

        for k,v in self.visited.items():
            if not v:
                return False
        return True

    
    def dfs(self, rooms,key):
        for room in rooms[key]:
            if self.visited[room]:
                continue
            else:
                self.visited[room] = True
                self.dfs(rooms,room)

if __name__ == "__main__":
    obj = keysAndRooms()
    print(obj.canVisitAllRooms([[]]))