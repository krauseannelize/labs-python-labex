# Complete the Space Mission Calculator

**Source:** [LabEx - Space Mission Calculator](https://labex.io/labs/python-space-mission-calculator-393156?course=quick-start-with-python)

In this challenge, you will complete a partially created Python module and use it in a main program.

## Tasks

1. Open the file [`space_math.py`](space_math.py).
2. Complete the three functions in `space_math.py`:
   - `calculate_fuel(distance)`
   - `time_to_destination(distance, speed)`
   - `gravity_force(mass1, mass2, distance)`
3. Open the file [`mission_planner.py`](mission_planner.py).
4. Import the functions from `space_math.py` and use them to calculate mission details.

## Requirements

- Complete the functions in `space_math.py` using the formulas provided in the comments.
- In `mission_planner.py`, import the functions from `space_math.py` using the `from ... import ...` syntax.
- Use the imported functions to calculate and display the mission details.
- Round all calculations to two decimal places in the output.

## Execution

To run the program, use the following command in your terminal:

```bash
python mission_planner.py
```

## Expected Output

```plaintext
Space Mission Details:
----------------------
Fuel needed: 112500000000.00 liters
Time to destination: 11250.00 hours
Gravitational force at destination: 12.64 N
```
