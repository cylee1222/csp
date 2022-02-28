def backtracking(assignment, slots, depth):
    if (depth == len(assignment)):
        return True
    global subs
    global rooms
    sub = subs[depth][0]
    available = subs[depth][2:]
    category = subs[depth][1]
    if (category == "c"):
        for slot in available:
            if (slots[slot] == -1):
                assignment[depth] = [sub, slot, rooms[0]]
                slots[slot] = rooms[0]
                if (backtracking(assignment, slots, depth+1)):
                    return True
                else:
                    slots[slot] = -1
                    assignment[depth] = [sub, -1, -1]
        else:
            return False

    elif (category == "o"):
        for slot in available:
            if (slots[slot] == -1):
                assignment[depth] = [sub, slot, rooms[0]]
                slots[slot] = [rooms[0]]
                if (backtracking(assignment, slots, depth+1)):
                    return True
                else:
                    slots[slot] = -1
                    assignment[depth] = [sub, -1, -1]
            elif (type(slots[slot]) == list):
                asRooms = slots[slot]
                temp = asRooms[:]
                if (len(asRooms) == len(rooms)):
                    continue
                asRooms.append(rooms[len(asRooms)])
                assignment[depth] = [sub, slot, asRooms[-1]]
                slots[slot] = asRooms
                if (backtracking(assignment, slots, depth+1)):
                    return True
                else:
                    slots[slot] = temp
                    assignment[depth] = [sub, -1, -1]
        else:
            return False

subs = [['FYP1', 'c', 'Mo3', 'Mo2'], ['FYP2', 'c', 'Tu1', 'We1'], ['FYP3', 'c', 'Mo1', 'We2'], [
    'FYP4', 'c', 'Mo2', 'We4'], ['FYP5', 'c', 'Mo2', 'We5'], ['FYP6', 'c', 'Mo2', 'Mo3'], ['FYP7', 'c', 'Mo3', 'We2']]
rooms = ['R1', 'R2', 'R3']

slots = {}
assignment = []

for sub in subs:
    for slot in sub[2:]:
        if (slot not in slots):
            slots[slot] = -1
    assignment.append([sub[0], -1, -1])

print("\nsubs:", subs)
print("\nrooms:", rooms)
print("\nslots:", slots)
print("\nassignment:", assignment)

result = backtracking(assignment, slots, 0)

print("\nslot result:", slots)

if (result):
    print("\nschedule: ")
    for sub in assignment:
        print(sub)
