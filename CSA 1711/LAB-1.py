from collections import deque

def get_neighbors(state):
    """Generates all valid next states by moving the blank tile (0)."""
    neighbors = []
    # Find the index of the blank space (0)
    blank_idx = state.index(0)
    
    # Convert 1D index to 2D row and column positions
    row, col = blank_idx // 3, blank_idx % 3
    
    # Possible directional moves for the blank tile: (row_change, col_change, move_name)
    moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]
    
    for dr, dc, move_name in moves:
        new_row, new_col = row + dr, col + dc
        
        # Verify if the new position stays within the 3x3 grid boundaries
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Convert 2D position back to 1D index
            new_blank_idx = new_row * 3 + new_col
            
            # Create a new state by swapping the blank space with the target tile
            new_state = list(state)
            new_state[blank_idx], new_state[new_blank_idx] = new_state[new_blank_idx], new_state[blank_idx]
            neighbors.append((tuple(new_state), move_name))
            
    return neighbors

def solve_8_puzzle(start_state, goal_state):
    """Solves the 8-puzzle problem using Breadth-First Search (BFS)."""
    # Queue stores: (current_state, path_taken)
    queue = deque([(start_state, [])])
    
    # Set to keep track of already explored states to avoid infinite loops
    visited = {start_state}
    
    while queue:
        current_state, path = queue.popleft()
        
        # Check if the target goal state is reached
        if current_state == goal_state:
            return path
            
        # Explore valid moves from the current configuration
        for neighbor, move_name in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [move_name]))
                
    return None # Returns None if the puzzle is unsolvable

def print_grid(state):
    """Helper function to print the 1D state representation as a 3x3 matrix."""
    for i in range(0, 9, 3):
        print(f" {state[i]} {state[i+1]} {state[i+2]} ")
    print()

# --- Example Execution ---
if __name__ == "__main__":
    # Define start and goal configurations (0 represents the empty block)
    initial = (1, 2, 3, 
               4, 0, 6, 
               7, 5, 8)
               
    goal = (1, 2, 3, 
            4, 5, 6, 
            7, 8, 0)

    print("Initial State:")
    print_grid(initial)
    
    print("Goal State:")
    print_grid(goal)
    
    solution_path = solve_8_puzzle(initial, goal)
    
    if solution_path is not None:
        print(f"Success! Puzzle solved in {len(solution_path)} moves.")
        print("Sequence of moves:", " -> ".join(solution_path))
    else:
        print("This initial state is unsolvable.")
