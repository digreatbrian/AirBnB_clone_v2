#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# All States
all_states = fs.all(State)
print(f"All States: {len(all_states.keys())}")
for state_key, val in all_states.items():
    print(val)

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print(f"New State: {new_state}")

# All States
all_states = fs.all(State)
print(f"All States: {len(all_states.keys())}")
for state_key, val in all_states.items():
    print(val)

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print(f"Another State: {another_state}")

# All States
all_states = fs.all(State)
print(f"All States: {len(all_states.keys())}")
for state_key, val in all_states.items():
    print(val)

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {len(all_states.keys())}")
for state_key, val in all_states.items():
    print(val)
