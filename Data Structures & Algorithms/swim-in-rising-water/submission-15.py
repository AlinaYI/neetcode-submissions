class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    
    def find(self, node):
        curr = node
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr

    def union(self, u, v):
        rootU, rootV = self.find(u), self.find(v)

        if rootU == rootV:
            return False
        
        if self.size[rootU] < self.size[rootV]:
            rootU, rootV = rootV, rootU
        
        self.parent[rootV] = rootU
        self.size[rootU] += self.size[rootV]
        return True

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        dsu
        把所有的cell变成一个node，然后排序
        一个node，一个node 连接
        如果当前的node是右下角的， 就return 当前的hight, 就直接return
        tc: O(mnlogmn) sc: Omn

        binary search 
        因为这里的答案是单调的，每次path都要取最大的，所以这里可以用binary search
        range 就是grid[0][0] -- len(grid)*len(grid)
        如果当前的mid， 带入能从左上跑到右下，那就是valid， 然后再看有没有比这个更小的值
        tc: (binary search 次数)log(mn) * mn (每次dfs的tc)
        sc: O(mn) --> seen

        dijkstra
        就是把这个当成weighted map看，加入minHeap，每次选尽量小的值
        直到到右下
        不用建graph，直接用grid来search 四个方向
        tc: Omn * logmn --> heap logmn
        sc: Omn
        '''

        row, col = len(grid), len(grid[0])
        dsu = DSU(row*col)

        edges = []
        for i in range(row):
            for j in range(col):
                edges.append((grid[i][j], i, j))
        
        edges.sort()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = set()
        for height, i, j in edges:
            seen.add((i,j))
            curr = col*i+j

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and (ni, nj) in seen:
                    nei = col*ni+nj
                    dsu.union(curr, nei)
            
            if dsu.find(0) == dsu.find(row*col-1):
                return height


        