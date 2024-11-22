floor = int(input())
room_each_floor = int(input())

for f in range(floor,0, -1):
    for r in range(0, room_each_floor):
        if f == floor:
            print(f"L{f}{r}", end=" ")

        elif f % 2 == 0:
            print(f"O{f}{r}", end=" ")
        elif f % 2 != 0:
            print(f"A{f}{r}", end=" ")

    print()