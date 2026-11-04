import random
import math

def simulated_annealing():
    current = 10
    t = 1

    print("SIMULATED ANNEALING ALGORITHM")
    print("-" * 35)
    print("Initial State:", current)

    while True:
        T = max(10 - 0.5 * t, 0)

        if T == 0:
            break

        next_state = current + random.choice([-3, -1, 1, 2])
        delta_E = next_state - current

        if delta_E > 0:
            current = next_state
            status = "Accepted (Better)"
        elif random.random() < math.exp(delta_E / T):
            current = next_state
            status = "Accepted (Probability)"
        else:
            status = "Rejected"

        print("Iteration:", t, "| Temperature:", round(T, 2),
              "| Current State:", current, "|", status)

        t += 1

    print("-" * 35)
    print("Final Solution:", current)
    print("Total Iterations:", t - 1)
    print("Algorithm Completed Successfully!")

simulated_annealing()
