import os
import time
import random
# Initialisation de la grille
grid_size = 50
grid = [[random.choice([0, 1]) for _ in range(grid_size)] for _ in range(grid_size)]



def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran
    for row in grid:
        print(' '.join(['*' if cell else '.' for cell in row]))
    time.sleep(1)  # Délai pour visualiser l'évolution

def count_neighbors(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):  
                new_x, new_y = x + i, y + j
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    count += grid[new_x][new_y]

    return count

def next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)] 
    
    for i in range(rows):
        for j in range(cols):
            neighbors=count_neighbors(grid, i, j)
            
            if grid[i][j]==1 and  (neighbors > 3 or neighbors < 2) : 
                    new_grid[i][j]=0
               
            elif grid[i][j]==0 and neighbors == 3 :
                    new_grid[i][j]=1
            else: 
                new_grid[i][j] = grid[i][j]
    
    return new_grid
                    
            
            
            
    



#%% 

while True:
    print_grid(grid)
    grid=next_generation(grid)

    
     
