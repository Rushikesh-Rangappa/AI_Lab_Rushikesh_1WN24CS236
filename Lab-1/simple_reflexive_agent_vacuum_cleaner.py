A = 'Dirty'
B = 'Clean' 

rooms = [A, B]
def vacuum_cleaner_agent(rooms):
    for i in range(len(rooms)):
        if rooms[i] == 'Dirty':
            rooms[i] = 'Clean'
        elif rooms[i] == 'Clean':
            pass
        else:
            return 'invalid'
    return rooms

print("Before cleaning:", rooms)
vacuum_cleaner_agent(rooms)
print("After cleaning:", rooms)
