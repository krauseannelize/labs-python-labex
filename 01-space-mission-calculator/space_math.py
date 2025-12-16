# Space Math Module

def calculate_fuel(distance):
    # Calculate fuel needed for the journey
    fuel = distance * 500
    return fuel

def time_to_destination(distance, speed):
    # Calculate time to reach the destination
    time = distance / speed
    return time

def gravity_force(mass1, mass2, distance):
    # Calculate the gravitational force between two objects
    G = 6.67430e-11 # gravitational constant 
    force = (G * mass1 * mass2) / (distance ** 2)
    return force
