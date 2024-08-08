import heapq

# Goal state of the 8-puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]


class PuzzleState:
    def __init__(self, board, parent=None, move=""):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.board == other.board

    def __lt__(self, other):
        return False

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.board])

    def is_goal(self):
        return self.board == goal_state

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def get_children(self):
        children = []
        blank_pos = self.get_blank_position()
        possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up movements

        for move in possible_moves:
            new_board = [row[:] for row in self.board]
            new_row, new_col = blank_pos[0] + move[0], blank_pos[1] + move[1]

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Perform the move
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_row][new_col] = \
                    new_board[new_row][new_col], new_board[blank_pos[0]][blank_pos[1]]
                children.append(PuzzleState(new_board, self, move))

        return children

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    target_row, target_col = (self.board[i][j] - 1) // 3, (self.board[i][j] - 1) % 3
                    distance += abs(i - target_row) + abs(j - target_col)
        return distance

    def total_cost(self):
        return self.depth + self.manhattan_distance()


def solve_puzzle(initial_state):
    priority_queue = []
    heapq.heappush(priority_queue, (initial_state.total_cost(), initial_state))
    visited = set()
    visited.add(tuple(map(tuple, initial_state.board)))

    while priority_queue:
        current_state = heapq.heappop(priority_queue)[1]

        if current_state.is_goal():
            return current_state

        for child in current_state.get_children():
            if tuple(map(tuple, child.board)) not in visited:
                heapq.heappush(priority_queue, (child.total_cost(), child))
                visited.add(tuple(map(tuple, child.board)))

    return None


def print_solution(solution):
    path = []
    current = solution
    while current:
        path.append(current)
        current = current.parent
    path.reverse()

    print("Steps to solve the 8-Puzzle:")
    for i, state in enumerate(path):
        print(f"Move {i + 1}: {state.move}")
        print(state)
        print()

# Example usage:
if __name__ == "__main__":
    initial_board = [[1, 2, 3],
                     [4, 0, 6],
                     [7, 5, 8]]

    initial_state = PuzzleState(initial_board)
    solution = solve_puzzle(initial_state)

    if solution:
        print_solution(solution)
    else:
        print("No solution found for the 8-Puzzle.")
