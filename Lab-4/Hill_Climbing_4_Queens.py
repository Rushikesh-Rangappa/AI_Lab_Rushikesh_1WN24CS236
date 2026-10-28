
import random

N = 4

# Calculate the number of pairs of queens attacking each other
def heuristic(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate the best neighboring state
def get_neighbor(state):
    neighbors = []

    for i in range(N):
        for j in range(i + 1, N):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(new_state)

    return min(neighbors, key=heuristic)


# Hill-climbing algorithm
def hill_climbing():
    current = random.sample(range(N), N)
    iteration = 1

    print("Initial state:", current)
    print("Initial conflicts:", heuristic(current))

    while True:
        neighbor = get_neighbor(current)

        print(f"Iteration {iteration}: "
              f"State = {neighbor}, "
              f"Conflicts = {heuristic(neighbor)}")

        if heuristic(neighbor) >= heuristic(current):
            break

        current = neighbor
        iteration += 1

        if heuristic(current) == 0:
            break

    return current, iteration


# Display the chessboard
def print_board(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
solution, iterations = hill_climbing()

print("\n--- Final Result ---")
print("Final state:", solution)
print("Number of conflicts:", heuristic(solution))
print("Iterations:", iterations)

if heuristic(solution) == 0:
    print("Status: Solution found!")
    print_board(solution)
else:
    print("Status: Local minimum reached. Restart may be needed.")
