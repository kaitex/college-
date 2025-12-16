from itertools import permutations

# --- Cryptarithmetic: SEND + MORE = MONEY ---
def solve_crypto(puzzle):
    letters = sorted(set("".join(puzzle)))
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[w[0]] == 0 for w in puzzle): 
            continue
        values = [int("".join(str(mapping[c]) for c in w)) for w in puzzle]
        if sum(values[:-1]) == values[-1]:
            return dict(zip(puzzle, values))
    return None

# --- N Queens ---
def solve_nqueens(N):
    def safe(board, r, c): 
        return all(board[i]!=c and abs(board[i]-c)!=r-i for i in range(r))
    def backtrack(r):
        if r==N: return [board[:]]
        return sum((backtrack(r+1) for c in range(N) if safe(board,r,c) and not board.__setitem__(r,c)),[])
    board=[-1]*N
    return backtrack(0)

# --- Water Jug Problem (4L, 3L -> goal 2L,0L) ---
def water_jug():
    cap1, cap2, goal, seen, stack = 4, 3, (2,0), set(), [(0,0)]
    while stack:
        j1,j2=stack.pop()
        if (j1,j2)==goal: return (j1,j2)
        if (j1,j2) in seen: continue
        seen.add((j1,j2))
        stack += [(cap1,j2),(j1,cap2),(0,j2),(j1,0),
                  (j1-min(j1,cap2-j2), j2+min(j1,cap2-j2)),
                  (j1+min(j2,cap1-j1), j2-min(j2,cap1-j1))]

# --- Run ---
if __name__=="__main__":
    print("Cryptarithm:", solve_crypto(['SEND','MORE','MONEY']))
    print("One N-Queens solution (N=4):", solve_nqueens(4)[0])
    print("Water Jug reaches:", water_jug())

