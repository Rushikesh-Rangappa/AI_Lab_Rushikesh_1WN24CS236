
# Forward Chaining Algorithm in First Order Logic (FOL)

# Knowledge Base: Initial Facts
facts = {
    ("American", "Robert"),
    ("Missile", "T1"),
    ("Owns", "A", "T1"),
    ("Enemy", "A", "America")
}

# Rules: (Premises, Conclusion)
rules = [
    # Missile(x) -> Weapon(x)
    ([("Missile", "?x")],
     ("Weapon", "?x")),

    # Missile(x) AND Owns(A,x) -> Sells(Robert,x,A)
    ([("Missile", "?x"), ("Owns", "A", "?x")],
     ("Sells", "Robert", "?x", "A")),

    # Enemy(x, America) -> Hostile(x)
    ([("Enemy", "?x", "America")],
     ("Hostile", "?x")),

    # American(p) AND Weapon(q) AND Sells(p,q,r)
    # AND Hostile(r) -> Criminal(p)
    ([("American", "?p"),
      ("Weapon", "?q"),
      ("Sells", "?p", "?q", "?r"),
      ("Hostile", "?r")],
     ("Criminal", "?p"))
]


# Unification function
def unify(pattern, fact, substitution):
    if pattern[0] != fact[0]:
        return None

    if len(pattern) != len(fact):
        return None

    new_sub = substitution.copy()

    for p, f in zip(pattern[1:], fact[1:]):

        if p.startswith("?"):
            if p in new_sub:
                if new_sub[p] != f:
                    return None
            else:
                new_sub[p] = f

        elif p != f:
            return None

    return new_sub


# Substitute variables with their values
def substitute(expression, substitution):
    return tuple(
        substitution.get(item, item)
        if isinstance(item, str) else item
        for item in expression
    )


# Find all possible substitutions for rule premises
def find_substitutions(premises, knowledge_base):

    if not premises:
        return [{}]

    results = []

    first = premises[0]
    remaining = premises[1:]

    for fact in knowledge_base:
        sub = unify(first, fact, {})

        if sub is not None:
            updated = [
                substitute(p, sub) for p in remaining
            ]

            for result in find_substitutions(updated, knowledge_base):
                combined = sub.copy()
                combined.update(result)
                results.append(combined)

    return results


# Forward Chaining Algorithm
def forward_chaining(KB, rules, query):

    new = set()

    while True:

        new.clear()

        for premises, conclusion in rules:

            substitutions = find_substitutions(
                premises, KB
            )

            for sub in substitutions:

                inferred = substitute(conclusion, sub)

                if inferred not in KB:
                    new.add(inferred)

        # If no new facts are inferred
        if not new:
            break

        # Add newly inferred facts to KB
        KB.update(new)

        print("\nNew facts inferred:")
        for fact in new:
            print(fact)

        # Check whether query is proved
        if query in KB:
            return True

    return query in KB


# Query to prove
query = ("Criminal", "Robert")

# Run Forward Chaining
print("Initial Knowledge Base:")
for fact in sorted(facts):
    print(fact)

print("\nStarting Forward Chaining...\n")

result = forward_chaining(facts, rules, query)

print("\nFinal Result:")

if result:
    print("Robert is Criminal: TRUE")
else:
    print("Robert is Criminal: FALSE")
