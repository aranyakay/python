
#rotten orange
#lC994


class Solution:
    def orangesRotting(self, grid) :
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        rotlist = list()
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] ==2:
                    rotlist.append([i, j])
        
        minute = 0
        while(len(rotlist)>0):
            newrotlist = list()
            for n in rotlist:
                x0 = n[0]
                y0 = n[1]
                for k, kx in enumerate(dx):
                    x = x0 + kx
                    y = y0 + dy[k]
                    if 0<= x < len(grid) and 0<=y< len(grid[0]) and grid[x][y]==1:
                        grid[x][y] = 2
                        newrotlist.append([x, y])
            if len(newrotlist)==0:
                break
            rotlist = newrotlist
            minute = minute + 1
        for i, row in enumerate(grid):
            if 1 in row:
                minute = -1
        return(minute)
                        
            
