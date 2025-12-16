def add_mission(missions, mission_details, name, details):
    # .append() adds mission name to ordered List
    missions.append(name)
    # Mapping name to a dictionary of details in dictionary
    mission_details[name] = details
    print("\nMission added successfully!")

def update_mission(mission_details, name, key, value):
    # Check for existence to avoid KeyError when updating nested dicts
    if name in mission_details:
        mission_details[name][key] = value
        print(f"\nMission {name} updated {key} successfully.")
    else:
        print(f"\nMission {name} not found.")

def display_missions(missions, mission_details):
    if missions:
        # Manually count missions for display purposes
        n = 1
        print("\nAll Missions:")
        for name in missions:
            print(f"{n}. {name}")
            for key, value in mission_details[name].items():
                print(f"   {key}: {value}")
            n += 1
    else:
        print("\nMission list is empty.")

def list_astronauts(mission_details):
    # Using a Set to automatically handle duplicate names across missions
    all_astronauts = set()
    for name, details in mission_details.items():
        # .get() provides a fallback empty string if 'Crew' key is missing
        crew_string = details.get('Crew', '')
        # Split string into list and filter out any empty strings
        crew_list = filter(None, crew_string.split(", "))
        # .update() adds all elements of a list to the set at once
        all_astronauts.update(crew_list)
    return all_astronauts

def main():
    # Initialize main data structures
    missions = []
    mission_details = {}

    while True:
        print("\nSpace Mission Management System")
        print("1. Add Mission")
        print("2. Update Mission")
        print("3. Display Missions")
        print("4. List Astronauts")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Enter mission name: ")
            destination = input("Enter destination: ")
            launch_date = input("Enter launch date: ")
            crew = input("Enter crew members (comma-separated): ")
            details = {
                "Destination": destination,
                "Launch Date": launch_date,
                "Crew": crew
            }
            # Passing local variables as arguments to functions
            add_mission(missions, mission_details, name, details)

        elif choice == '2':
            name = input("Enter mission name to update: ")
            key = input("Enter detail to update (Destination/Launch Date/Crew): ")
            value = input(f"Enter new value for {key}: ")
            update_mission(mission_details, name, key, value)

        elif choice == '3':
            display_missions(missions, mission_details)

        elif choice == '4':
            astronauts = list_astronauts(mission_details)
            print("\nAll Astronauts:")
            # sorted() makes output look cleaner
            for astronaut in sorted(astronauts):
                print(f"- {astronaut}")

        elif choice == '5':
            print("Exiting Space Mission Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# This ensures the code only runs if the script is executed directly, 
# and not if it's imported as a module in another file.
if __name__ == "__main__":
    main()
