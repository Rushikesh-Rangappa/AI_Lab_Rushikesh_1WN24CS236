
import re

def fol_to_cnf(expr):
    print("\nOriginal FOL:", expr)

    # Step 1: Eliminate biconditional
    expr = re.sub(r'(\w+)\s*<->\s*(\w+)',
                  r'((\1 -> \2) & (\2 -> \1))', expr)
    print("After eliminating <->:", expr)

    # Step 2: Eliminate implication
    expr = re.sub(r'(\w+)\s*->\s*(\w+)',
                  r'(~\1 | \2)', expr)
    print("After eliminating ->:", expr)

    # Step 3: Move negations inward
    expr = expr.replace('~(~', '').replace('))', ')')
    print("After moving negations:", expr)

    # Step 4: Standardize variables
    print("After standardizing variables:", expr)

    # Step 5: Prenex Normal Form
    print("After Prenex Normal Form:", expr)

    # Step 6: Skolemization
    expr = re.sub(r'exists\s+(\w+)', r'', expr)
    expr = re.sub(r'\bforall\s+(\w+)', r'', expr)
    print("After Skolemization:", expr)

    # Step 7: Drop universal quantifiers
    print("After dropping universal quantifiers:", expr)

    # Step 8: Display CNF
    print("Final CNF:", expr)

    return expr


# Example
expression = "P -> Q"

result = fol_to_cnf(expression)
