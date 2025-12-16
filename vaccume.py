# Simple Reflex Vacuum Cleaner

def reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    return "Right" if location == "A" else "Left"

rooms = {"A": "Dirty", "B": "Dirty"}   # initial states
location = "A"                         # agent start

for _ in range(10):
    status = rooms[location]
    action = reflex_agent(location, status)
    print(f"Location: {location}, Status: {status}, Action: {action}")

    if action == "Suck":
        rooms[location] = "Clean"
    else:
        location = "B" if location == "A" else "A"

    if rooms["A"] == rooms["B"] == "Clean":
        print("All clean. Stopping.")
        break
