
import heapq

def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g

        for neighbor, cost in graph[current].items():
            new_g = g + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                came_from[neighbor] = current
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    open_list, (new_f, new_g, neighbor)
                )

    return None, float("inf")


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

path, cost = astar(graph, heuristic, 'A', 'D')

print("Shortest Path:", path)
print("Total Cost:", cost)
