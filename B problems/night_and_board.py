from collections import deque

def get_moves(x, y, a, b, n):
    moves = [
        (x+a, y+b), (x+a, y-b), (x-a, y+b), (x-a, y-b),
        (x+b, y+a), (x+b, y-a), (x-b, y+a), (x-b, y-a)
    ]
    return [(x, y) for x, y in moves if 0 <= x < n and 0 <= y < n]

def bfs(a, b, n):
    queue = deque([(0, 0, 0)])  # (x, y, moves)
    visited = set([(0, 0)])

    while queue:
        x, y, moves = queue.popleft()
        
        if x == n-1 and y == n-1:
            return moves
        
        for nx, ny in get_moves(x, y, a, b, n):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))
    
    return -1  

def solve_knightl(n):
    results = []
    for i in range(1, n):
        row = []
        for j in range(1, n):
            moves = bfs(i, j, n)
            row.append(str(moves))
        results.append(' '.join(row))
    return results

# Main execution
n = int(input().strip())
output = solve_knightl(n)
for row in output:
    print(row)