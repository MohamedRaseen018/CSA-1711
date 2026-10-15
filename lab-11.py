
def is_safe(region, color, assignment, graph):
    for neighbor in graph[region]:
        if assignment.get(neighbor) == color:
            return False
    return True


def map_coloring(graph, colors, assignment):
    if len(assignment) == len(graph):
        return True

    region = next(r for r in graph if r not in assignment)

    for color in colors:
        if is_safe(region, color, assignment, graph):
            assignment[region] = color

            if map_coloring(graph, colors, assignment):
                return True

            del assignment[region]

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
assignment = {}

if map_coloring(graph, colors, assignment):
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution exists")
