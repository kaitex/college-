from itertools import permutations

def solve_crypto(puzzle):
    letters = sorted(set("".join(puzzle)))
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        # Check that no word starts with zero
        if any(mapping[w[0]] == 0 for w in puzzle):
            continue
        # Convert words to numbers
        values = [int("".join(str(mapping[c]) for c in w)) for w in puzzle]
        # Check if sum of all but last equals last
        if sum(values[:-1]) == values[-1]:
            return dict(zip(puzzle, values))
    return None

# Function call
print("Cryptarithm:", solve_crypto(['SEND','MORE','MONEY']))
