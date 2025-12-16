# Complete the Space Mission Management System

**Source:** [LabEx - Space Mission Management System](https://labex.io/labs/python-space-mission-management-system-393176?course=quick-start-with-python)

In this challenge, you will complete a partially created Python script that manages space missions using different data structures.

## Tasks

1. Open the file [`mission_control.py`]().
2. Complete the four functions in `mission_control.py`:
   - `add_mission(missions, mission_details, name, details)`
   - `update_mission(mission_details, name, key, value)`
   - `display_missions(missions, mission_details)`
   - `list_astronauts(mission_details)`
3. Run the script and test the functionality by adding a mission, updating it, displaying all missions, and listing astronauts.

## Requirements

- Complete the functions in `mission_control.py` using the appropriate data structures:
  - Use the `missions` list to store mission names
  - Use the `mission_details` dictionary to store details of each mission
  - Use a set to store unique astronaut names in the `list_astronauts` function
- Ensure that the `add_mission` function adds the new mission to both the `missions` list and the `mission_details` dictionary
- The `update_mission` function should modify the specified detail of the given mission
- The `display_missions` function should print all missions and their details
- The `list_astronauts` function should return a set of all unique astronauts across all missions

## Execution

To run the program, use the following command in your terminal:

```bash
python mission_control.py
```

## Expected Output

```plaintext
Space Mission Management System
1. Add Mission
2. Update Mission
3. Display Missions
4. List Astronauts
5. Exit

Enter your choice: 1
Enter mission name: Mars Expedition
Enter destination: Mars
Enter launch date: 2030-01-01
Enter crew members (comma-separated): John Doe, Jane Smith

Mission added successfully!

Enter your choice: 3

All Missions:
1. Mars Expedition
   Destination: Mars
   Launch Date: 2030-01-01
   Crew: John Doe, Jane Smith

Enter your choice: 4

All Astronauts:
- John Doe
- Jane Smith

Enter your choice: 5
Exiting Space Mission Management System. Goodbye!
```
