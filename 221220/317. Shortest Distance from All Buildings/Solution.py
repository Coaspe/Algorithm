def __init__(self):
    self.empty, self.building = 0, 1

    self.direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def shortestDistance(self, grid: List[List[int]]) -> int:
    buildings = []
    candidate_lands = {}  # {position, distance}

    # 1. Find all buildings and candidate empty lands
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == self.building:
                buildings.append((r, c))

            elif grid[r][c] == self.empty:
                candidate_lands[(r, c)] = 0

    # 2. Compute min distance from each building to all candidate empty lands
    for building_position in buildings:
        self.compute_shortest_distances_bfs(candidate_lands, building_position)

    return min(candidate_lands.values()) if buildings and candidate_lands else -1


def compute_shortest_distances_bfs(self, candidate_lands: dict, position: (int, int)):
    distance = 0
    visited = set()

    # 1. BFS: this 2-lists bfs traversal makes it possible to avoid storing the distance for each node
    curr_level = [position]
    while curr_level:
        distance += 1

        next_level = []
        for position in curr_level:
            for direction in self.direction:
                adjacent_position = (
                    position[0] + direction[0], position[1] + direction[1])

                if adjacent_position in candidate_lands and adjacent_position not in visited:
                    candidate_lands[adjacent_position] += distance

                    visited.add(adjacent_position)
                    next_level.append(adjacent_position)

        curr_level = next_level

    # 2. All empty lands that are not reachable from a building are excluded
    if len(visited) != len(candidate_lands):
        for position in set(candidate_lands.keys()).difference(visited):
            candidate_lands.pop(position)
