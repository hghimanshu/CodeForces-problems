from heapq import heappop, heappush, heapify

class Solution:
    def minimumEffortPath(self, heights):
        minEffort = 0
        rows = len(heights)
        cols = len(heights[0])
        currHeight = heights[0][0]
        startCoord = (0,0)
        processed = {startCoord:currHeight}
        queue = [(currHeight,startCoord)]
        heapify(queue)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            node = heappop(queue)
            minEffort = max(minEffort,node[0]-currHeight)
            if node[1] in processed:
                continue
            currHeight = node[0]
            if node[1] == (rows-1,cols-1):
                return minEffort
            processed[node[1]] = currHeight

            for dx,dy in dirs:
                X,Y = node[1][0]+dx,node[1][1]+dy
                if (X,Y) in processed: 
                    continue
                if X < 0 or X >= rows or Y < 0 or Y >= cols:
                    continue
                heappush(queue,(heights[X][Y],(X,Y)))

        return minEffort
        


if __name__ == '__main__':
    # heights = [[1,2,2],[3,8,2],[5,3,5]]
    heights = [[1,2,3],[3,8,4],[5,3,5]]
    sol = Solution()
    print(sol.minimumEffortPath(heights))
