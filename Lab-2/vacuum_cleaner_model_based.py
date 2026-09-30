rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

state = [location, rooms["A"], rooms["B"]]

memory_stack = []

memory_stack.append(state.copy())

while rooms["A"] != "Clean" or rooms["B"] != "Clean":

    print("Location:", location)
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])

    state = [location, rooms["A"], rooms["B"]]
    memory_stack.append(state.copy())

    if rooms[location] == "Dirty":
        print("Suck")
        rooms[location] = "Clean"
        memory_stack.append("Suck")

    if location == "A" and rooms["B"] == "Dirty":
        location = "B"
        print("Move to B")
        memory_stack.append("Move")

    elif location == "B" and rooms["A"] == "Dirty":
        location = "A"
        print("Move to A")
        memory_stack.append("Move")

    elif rooms["A"] == "Clean" and rooms["B"] == "Clean":
        memory_stack.append("Stop")
        print("Stop")
        break

print("\nMemory Stack:")
print(memory_stack)
