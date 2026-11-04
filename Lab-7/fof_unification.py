def unify(x, y, subs=None):
    if subs is None:
        subs = {}

    if x == y:
        return subs

    if isinstance(x, str) and x.islower():
        if x in subs:
            return unify(subs[x], y, subs)
        if y in subs:
            return unify(x, subs[y], subs)
        if occurs(x, y):
            return None
        subs[x] = y
        return subs

    if isinstance(y, str) and y.islower():
        return unify(y, x, subs)

    if isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0] or len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):
            subs = unify(a, b, subs)
            if subs is None:
                return None
        return subs

    return None


def occurs(var, expr):
    if var == expr:
        return True
    if isinstance(expr, tuple):
        return any(occurs(var, item) for item in expr)
    return False


# Example expressions
expr1 = ("Eats", "x", "Apple")
expr2 = ("Eats", "Riya", "y")

print("FIRST ORDER LOGIC - UNIFICATION")
print("--------------------------------")

print("Expression 1:", expr1)
print("Expression 2:", expr2)

result = unify(expr1, expr2)

if result is not None:
    print("\nUnification Successful!")
    print("Substitution:", result)
    print("Unified Expression: Eats(Riya, Apple)")
else:
    print("\nUnification Failed!")
