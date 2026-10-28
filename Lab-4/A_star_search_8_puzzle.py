import heapq

# 0 represents the blank space. Goal is 1-8 followed by 0.
GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
GOAL_POS = {num: (r, c) for r, row in enumerate(GOAL) for c, num in enumerate(row)}

def manhattan(board):
    """Calculates total distance of tiles from their target positions."""
    return sum(abs(r - GOAL_POS[val][0]) + abs(c - GOAL_POS[val][1])
               for r, row in enumerate(board) for c, val in enumerate(row) if val)

def get_neighbors(board):
    """Finds the blank space and yields all valid next board states."""
    r, c = next((r, c) for r, row in enumerate(board) for c, val in enumerate(row) if val == 0)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= r + dr < 3 and 0 <= c + dc < 3:
            nb = [list(row) for row in board]
            nb[r][c], nb[r + dr][c + dc] = nb[r + dr][c + dc], nb[r][c]
            yield tuple(tuple(row) for row in nb)

def solve(start):
    """A* Search: Returns a list of boards from start to goal, or None."""
    start = tuple(tuple(row) for row in start)
    # open_list stores tuples of: (f_score, g_score, current_board, path_taken)
    open_list = [(manhattan(start), 0, start, [start])]
    seen = {start}

    while open_list:
        _, g, board, path = heapq.heappop(open_list)

        if board == GOAL:
            return path

        for neighbor in get_neighbors(board):
            if neighbor not in seen:
                seen.add(neighbor)
                heapq.heappush(open_list, (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [neighbor]))
    return None

# --- Quick Test ---
if __name__ == "__main__":
    puzzle = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    solution = solve(puzzle)
    
    if solution:
        print(f"Solved in {len(solution) - 1} moves!")
        for step in solution:
            for row in step: print(*[x if x else '_' for x in row])
            print("---")
