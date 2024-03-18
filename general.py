import numpy as np
import matplotlib.pyplot as plt

class QuantumDot:
    def __init__(self, state=0):
        self.state = state  # 0 or 1
    
    def flip_state(self):
        self.state = 1 - self.state  # Flip the state (0 to 1, 1 to 0)

class QCA:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=np.int8)  # Initialize grid with zeros
        self.initialize_grid()  # Initialize quantum dots in the grid
    
    def initialize_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i, j] = np.random.randint(0, 2)  # Initialize quantum dot state randomly
    
    def update_grid(self):
        updated_grid = np.zeros((self.rows, self.cols), dtype=np.int8)  # Create a new grid for updated states
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors_sum = np.sum(self.get_neighbors(i, j))  # Sum of neighbor states
                updated_grid[i, j] = self.apply_rule(neighbors_sum)  # Apply QCA rule based on neighbors
        self.grid = updated_grid  # Update the grid
    
    def get_neighbors(self, i, j):
        neighbors = []
        for ni in range(i-1, i+2):
            for nj in range(j-1, j+2):
                if ni >= 0 and ni < self.rows and nj >= 0 and nj < self.cols:
                    if ni != i or nj != j:  # Exclude the current cell itself
                        neighbors.append(self.grid[ni, nj])
        return neighbors
    
    def apply_rule(self, neighbors_sum):
        # Simple majority voting rule: if more than half of neighbors are in state 1, switch state
        if neighbors_sum > 4:
            return 1
        else:
            return 0
    
    def plot_grid(self):
        plt.imshow(self.grid, cmap='binary', interpolation='nearest')
        plt.title('Quantum Dot Cellular Automata')
        plt.colorbar()
        plt.show()

# Example usage
rows, cols = 10, 10
qca_system = QCA(rows, cols)
qca_system.plot_grid()

# Run simulation for a few steps and plot the updated grid
for _ in range(5):
    qca_system.update_grid()
    qca_system.plot_grid()
