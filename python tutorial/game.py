from collections import deque

def bfs(N, M, grid, start, end):
    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Check if a cell is stable
    def is_stable(r, c):
        if r == N - 1:  # Last row is always stable
            return True
        if grid[r + 1][c] == 1:  # If there's a lift below
            return True
        return False

    # Gravity effect: Move down until we reach a stable cell
    def apply_gravity(r, c):
        while r < N - 1 and grid[r + 1][c] == 0:
            r += 1
        if is_stable(r, c):
            return r, c
        return r, c  # If no stable cell is reachable, return current position

    # BFS Queue: each element is (r, c, steps, lifts_used)
    queue = deque([(start[0], start[1], 0, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True
    
    # Start BFS
    while queue:
        r, c, steps, lifts_used = queue.popleft()

        # If we reach the destination cell
        if (r, c) == (end[0], end[1]):
            return steps + lifts_used  # Total cells + lifts used
        
        # Check all 4 possible directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Ensure within bounds and not visited
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if grid[nr][nc] == 1:  # Lift cell, can move upwards
                    visited[nr][nc] = True
                    queue.append((nr, nc, steps + 1, lifts_used + 1))
                elif grid[nr][nc] == 0:  # Empty cell, apply gravity
                    nr, nc = apply_gravity(nr, nc)
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc, steps + 1, lifts_used))
    
    return "Impossible"

def solve():
    # Input reading
    N, M = map(int, input().split())  # Read grid dimensions
    grid = [list(map(int, input().split())) for _ in range(N)]  # Read grid
    
    start_r, start_c = map(int, input().split())  # Start position
    end_r, end_c = map(int, input().split())  # End position
    
    # Call BFS to solve
    result = bfs(N, M, grid, (start_r, start_c), (end_r, end_c))
    print(result)

if __name__ =='__main__':
    main() 