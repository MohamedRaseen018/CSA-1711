from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # Queue for BFS, storing current state (x, y) and the path taken
    queue = deque([[(0, 0)]])
    visited = set([(0, 0)])
    
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        
        # Check if goal state is reached
        if x == target or y == target:
            return path
        
        # List of all possible next states
        transitions = [
            (jug1_capacity, y),          # Fill Jug 1
            (x, jug2_capacity),          # Fill Jug 2
            (0, y),                      # Empty Jug 1
            (x, 0),                      # Empty Jug 2
            # Pour Jug 1 -> Jug 2
            (max(0, x - (jug2_capacity - y)), min(jug2_capacity, x + y)),
            # Pour Jug 2 -> Jug 1
            (min(jug1_capacity, x + y), max(0, y - (jug1_capacity - x)))
        ]
        
        for state in transitions:
            if state not in visited:
                visited.add(state)
                queue.append(path + [state])
                
    return None

# Example usage: 4-liter jug, 3-liter jug, target 2 liters
solution = water_jug_bfs(4, 3, 2)
print("Steps to reach target:")
for step in solution:
    print(step)
