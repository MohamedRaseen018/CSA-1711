
from collections import deque

def is_valid(m, c):
    # Check whether the state is safe
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and c > m:
        return False
    if (3 - m) > 0 and (3 - c) > (3 - m):
        return False
    return True

def solve():
    # State: (missionaries_left, cannibals_left, boat_side)
    start = (3, 3, 1)
    goal = (0, 0, 0)

    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution found:\n")
            for step in path:
                print(step)
            print("\nTotal crossings:", len(path) - 1)
            return

        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)

            if is_valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    print("No solution exists.")

solve()
