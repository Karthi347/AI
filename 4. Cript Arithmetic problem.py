from itertools import permutations

def is_valid_solution(assignment, words, result):
    # Create a dictionary to map letters to digits
    mapping = dict(zip(letters, assignment))
    
    # Extract the digits for each word
    word_values = []
    for word in words:
        value = 0
        for char in word:
            value = value * 10 + mapping[char]
        word_values.append(value)
    
    # Calculate the value of the result word
    result_value = 0
    for char in result:
        result_value = result_value * 10 + mapping[char]
    
    # Check if the sum of the words equals the result value
    return sum(word_values) == result_value

def solve_cryptarithmetic(words, result):
    # Extract unique letters
    unique_letters = set("".join(words) + result)
    if len(unique_letters) > 10:
        print("Too many unique letters for a valid solution.")
        return None

    # Convert unique_letters to a sorted list
    global letters
    letters = sorted(list(unique_letters))

    for perm in permutations(digits, len(letters)):
        # Check if any leading letter is zero
        leading_letters = {word[0] for word in words + [result]}
        if any(perm[letters.index(letter)] == 0 for letter in leading_letters):
            continue
        if is_valid_solution(perm, words, result):
            return dict(zip(letters, perm))
    return None

# User input
equation = input("Enter the crypt-arithmetic equation (e.g., SEND + MORE = MONEY): ")
# Parse the equation
words_part, result_part = equation.split('=')
words = [word.strip() for word in words_part.split('+')]
result = result_part.strip()

# Create a list of digits from 0 to 9
digits = list(range(10))

# Solve the puzzle
solution = solve_cryptarithmetic(words, result)

# Print the solution
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter} = {digit}")
else:
    print("No solution found")
