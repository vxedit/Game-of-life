import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def initialize_grid(size):
    return np.random.choice([0, 1], size*size, p=[0.7, 0.3]).reshape(size, size)

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            total = int((grid[i, (j-1)%grid.shape[1]] + 
                         grid[i, (j+1)%grid.shape[1]] +
                         grid[(i-1)%grid.shape[0], j] + 
                         grid[(i+1)%grid.shape[0], j] +

                         grid[(i-1)%grid.shape[0], (j-1)%grid.shape[1]] + 
                         grid[(i-1)%grid.shape[0], (j+1)%grid.shape[1]] +
                         grid[(i+1)%grid.shape[0], (j-1)%grid.shape[1]] + 
                         grid[(i+1)%grid.shape[0], (j+1)%grid.shape[1]]
                         ))
            # 0=1>0 | 1=1>0 | 2,3=1>1 | 4,5,..=1>0 | 3=0>1 
            # die   | die   |  surviv |    die     | reviv  
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
                # elif (total == 2) or (total == 3):    # survival doest need condition
                #     new_grid[i,j] = 1
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

def animate(grid):
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    def update(frame):
        nonlocal grid
        grid = update_grid(grid)
        img.set_data(grid)
        return [img]

    ani = animation.FuncAnimation(fig, update, frames=10, interval=200, save_count=50)
    plt.show()

if __name__ == "__main__":
    grid = initialize_grid(100)
    animate(grid)
