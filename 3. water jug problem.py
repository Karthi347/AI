from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    if target_amount > max(jug1_capacity, jug2_capacity):
        return "Target amount cannot be greater than the capacity of the larger jug."

    # Initial state: both jugs are empty
    initial_state = (0, 0)
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        # Print the current state of the jugs
        print(f"Jug1: {jug1} liters, Jug2: {jug2} liters")

        # Check if target amount is reached
        if jug1 == target_amount or jug2 == target_amount:
            return f"Target amount {target_amount} liters can be measured."

        # Generate next possible states
        next_states = []

        # Fill jug1
        next_states.append((jug1_capacity, jug2) if jug1 < jug1_capacity else (jug1, jug2))

        # Fill jug2
        next_states.append((jug1, jug2_capacity) if jug2 < jug2_capacity else (jug1, jug2))

        # Empty jug1
        next_states.append((0, jug2))

        # Empty jug2
        next_states.append((jug1, 0))

        # Pour jug1 into jug2
        pour_amount = min(jug1, jug2_capacity - jug2)
        next_states.append((jug1 - pour_amount, jug2 + pour_amount))

        # Pour jug2 into jug1
        pour_amount = min(jug2, jug1_capacity - jug1)
        next_states.append((jug1 + pour_amount, jug2 - pour_amount))

        # Explore each next state
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    # If no solution found
    return f"Target amount {target_amount} liters cannot be measured."

# Get user input for jug capacities and target amount
while True:
    try:
        jug1_capacity = int(input("Enter the capacity of jug 1: "))
        jug2_capacity = int(input("Enter the capacity of jug 2: "))
        target_amount = int(input("Enter the target amount to measure: "))
        break
    except ValueError:
        print("Invalid input. Please enter valid integers for capacities and target amount.")

# Solve and print each step of the Water Jug Problem
print("\nSteps to measure the target amount:")
result = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
print(result)
