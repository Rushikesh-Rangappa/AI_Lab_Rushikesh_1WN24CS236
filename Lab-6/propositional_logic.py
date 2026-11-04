from itertools import product

def truth_table_entails():
    print("TRUTH TABLE ENUMERATION ALGORITHM")
    print("=" * 55)

    symbols = ['P', 'Q', 'R']
    models = []

    print("\nP  Q  R | Q->P | P->~Q | Q|R | KB")
    print("-" * 55)

    for P, Q, R in product([True, False], repeat=3):

        a = (not Q) or P
        b = (not P) or (not Q)
        c = Q or R

        KB = a and b and c

        print(f"{int(P)}  {int(Q)}  {int(R)} |"
              f"  {int(a)}  |   {int(b)}   |"
              f"  {int(c)}  | {int(KB)}")

        if KB:
            models.append((P, Q, R))

    print("\n" + "=" * 55)
    print("MODELS OF KB:", models)

    # Question ii: Does KB entail R?
    q2 = all(R for P, Q, R in models)

    # Question iii: Does KB entail R -> P?
    q3 = all((not R) or P for P, Q, R in models)

    # Question iv: Does KB entail Q -> R?
    q4 = all((not Q) or R for P, Q, R in models)

    print("\nENTAILMENT RESULTS")
    print("-" * 55)
    print("ii) Does KB entail R?       :", "YES" if q2 else "NO")
    print("iii) Does KB entail R -> P? :", "YES" if q3 else "NO")
    print("iv) Does KB entail Q -> R?  :", "YES" if q4 else "NO")

    print("-" * 55)
    print("Algorithm executed successfully!")

truth_table_entails()
