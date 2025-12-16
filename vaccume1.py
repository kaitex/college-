def vacuum_world():

    goal = {'A': '0', 'B': '0'}
    cost = 0

    loc = input("Enter location of vacuum (A or B): ").upper()
    curr = input(f"Enter status of Room {loc} (0=clean, 1=dirty): ")
    other = input("Enter status of other room (0=clean, 1=dirty): ")

    # Cleaning action
    def clean(room):
        nonlocal cost
        goal[room] = '0'
        cost += 3
        print(f"Room {room} cleaned. Cost = {cost}")

    # Moving action
    def move(direction):
        nonlocal cost
        cost += 1
        print(f"I moved {direction}. Cost = {cost}")

    # --- Agent Logic ---
    if loc == 'A':
        print("Vacuum at A")

        if curr == '1':
            clean('A')

        if other == '1':
            move("RIGHT")
            clean('B')
        else:
            print("Room B already clean")

    elif loc == 'B':
        print("Vacuum at B")

        if curr == '1':
            clean('B')

        if other == '1':
            move("LEFT")
            clean('A')
        else:
            print("Room A already clean")

    else:
        print("Invalid location")
        return

    print("GOAL STATE:", goal)
    print("Total Cost:", cost)


# Call the function ONCE
vacuum_world()
