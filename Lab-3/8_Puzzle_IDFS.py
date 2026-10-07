def get_state(msg):
    while True:
        try:
            s = tuple(map(int, input(msg).split()))
            if len(s) == 9 and sorted(s) == list(range(9)):
                return s
            print("  ✗ Enter exactly 9 unique numbers (0–8).")
        except ValueError:
            print("  ✗ Numbers only. Try again.")


def moves(state):
    i = state.index(0)
    r, c = divmod(i, 3)
    result = []

    for dr, dc, name in [(-1, 0, "Up"), (1, 0, "Down"),
                         (0, -1, "Left"), (0, 1, "Right")]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            s = list(state)
            s[i], s[j] = s[j], s[i]
            result.append((tuple(s), name))

    return result


def dfs(state, goal, depth, path, visited):
    if state == goal:
        return path
    if depth == 0:
        return None

    visited.add(state)

    for new_state, move in moves(state):
        if new_state not in visited:
            ans = dfs(new_state, goal, depth - 1,
                      path + [move], visited)
            if ans:
                return ans

    visited.remove(state)
    return None


def iddfs(start, goal, max_depth=50):
    for depth in range(max_depth + 1):
        ans = dfs(start, goal, depth, [], set())
        if ans is not None:
            return ans
    return None


# Input
start = get_state("Initial state : ")
goal = get_state("Goal state    : ")

# Solve
solution = iddfs(start, goal)

# Output
print("\n" + "=" * 35)
print("         IDDFS RESULT")
print("=" * 35)

if solution == []:
    print("Status : Already at the goal.")
elif solution:
    print("Status : Solution found!")
    print("Moves  :", len(solution))
    print("Path   :", " → ".join(solution))
else:
    print("Status : No solution found.")

print("=" * 35)
