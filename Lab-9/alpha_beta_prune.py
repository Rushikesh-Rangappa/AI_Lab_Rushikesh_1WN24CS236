
def alphabeta(node, depth, alpha, beta, maximizing):
    if depth == 0 or not node["children"]:
        return node["value"]

    if maximizing:
        best = float('-inf')

        for child in node["children"]:
            val = alphabeta(child, depth-1, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print("Branch pruned!")
                break

        print("MAX value:", best)
        return best

    else:
        best = float('inf')

        for child in node["children"]:
            val = alphabeta(child, depth-1, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print("Branch pruned!")
                break

        print("MIN value:", best)
        return best


# Game tree
tree = {
    "value": 0,
    "children": [
        {"value": 0, "children": [
            {"value": 3, "children": []},
            {"value": 5, "children": []}
        ]},
        {"value": 0, "children": [
            {"value": 2, "children": []},
            {"value": 9, "children": []}
        ]}
    ]
}

print("ALPHA-BETA PRUNING")
print("------------------")

result = alphabeta(tree, 2, float('-inf'), float('inf'), True)

print("------------------")
print("Optimal Value:", result)
