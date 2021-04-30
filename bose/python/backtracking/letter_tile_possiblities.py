class Solution:

    def __init__(self):
        self.sets = set()

    def getTile(self,curr,seen,tiles,prev):
        self.sets.add(curr)
        if len(curr) > len(tiles):
            return
        

        for i in range(0,len(tiles)):
            # if i not in seen and tiles[i]!=prev:
            if i not in seen:
                curr+=tiles[i]
                seen.append(i)
                self.getTile(curr,seen,tiles,prev)
                curr= curr[:-1]
                prev_idx = seen.pop()
                prev = tiles[prev_idx]

    def numTilePossibilities(self, tiles):
        prev = ""
        for i in range(0,len(tiles)):
            if tiles[i]!=prev:
                self.getTile(tiles[i],[i],tiles,"")
            prev = tiles[i]
        

        return len(self.sets)

if __name__ == "__main__":
    sol = Solution()
    tiles = "AAABBC"
    print(sol.numTilePossibilities(tiles))
