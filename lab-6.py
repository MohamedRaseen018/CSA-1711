
# Vacuum Cleaner Problem

def vacuum_cleaner():
    rooms = {'A': 'Dirty', 'B': 'Dirty'}
    location = 'A'

    while 'Dirty' in rooms.values():
        print("Current Location:", location)

        if rooms[location] == 'Dirty':
            print("Room", location, "is Dirty. Cleaning...")
            rooms[location] = 'Clean'
        else:
            print("Room", location, "is already Clean.")

        if location == 'A':
            location = 'B'
        else:
            location = 'A'

    print("\nAll rooms are clean!")
    print("Final Status:", rooms)

vacuum_cleaner()
