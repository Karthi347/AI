class State:
    def __init__(self, left_missionaries, left_cannibals, boat_position):
        self.left_missionaries = left_missionaries
        self.left_cannibals = left_cannibals
        self.boat_position = boat_position  # 0 for left, 1 for right
    
    def is_valid(self):
        # Check if any side has negative numbers or if cannibals outnumber missionaries
        if self.left_missionaries < 0 or self.left_cannibals < 0 or \
           self.left_missionaries > 3 or self.left_cannibals > 3 or \
           (self.left_missionaries > 0 and self.left_cannibals > self.left_missionaries) or \
           (3 - self.left_missionaries > 0 and 3 - self.left_cannibals > 3 - self.left_missionaries):
            return False
        return True
    
    def is_goal(self):
        return self.left_missionaries == 0 and self.left_cannibals == 0 and self.boat_position == 1
    
    def __eq__(self, other):
        return self.left_missionaries == other.left_missionaries and \
               self.left_cannibals == other.left_cannibals and \
               self.boat_position == other.boat_position
    
    def __hash__(self):
        return hash((self.left_missionaries, self.left_cannibals, self.boat_position))
    
    def __str__(self):
        return f"Left: {self.left_missionaries} missionaries, {self.left_cannibals} cannibals | Boat: {'Right' if self.boat_position == 1 else 'Left'}"

def dfs(current_state, visited, path):
    if current_state.is_goal():
        path.append(current_state)
        return True
    
    visited.add(current_state)
    path.append(current_state)
    
    for next_state in get_next_states(current_state):
        if next_state not in visited:
            if dfs(next_state, visited, path):
                return True
    
    path.pop()
    return False

def get_next_states(current_state):
    next_states = []
    if current_state.boat_position == 0:
        for m in range(3):
            for c in range(3):
                if m + c >= 1 and m + c <= 2:
                    next_state = State(current_state.left_missionaries - m, current_state.left_cannibals - c, 1)
                    if next_state.is_valid():
                        next_states.append(next_state)
    else:
        for m in range(3):
            for c in range(3):
                if m + c >= 1 and m + c <= 2:
                    next_state = State(current_state.left_missionaries + m, current_state.left_cannibals + c, 0)
                    if next_state.is_valid():
                        next_states.append(next_state)
    return next_states

def print_solution(path):
    print("Solution to the Missionaries and Cannibals problem:")
    for i, state in enumerate(path):
        print(f"Step {i + 1}: {state}")
    print()

def main():
    initial_state = State(3, 3, 0)
    visited = set()
    path = []
    
    if dfs(initial_state, visited, path):
        print_solution(path)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
