[x+_x][y+_y] = 1
            dfs(arr, size+1, count+arr[x+_x][y+_y], x+_x, y+_y, check)
            check[x+_x][y+_y] = 0
