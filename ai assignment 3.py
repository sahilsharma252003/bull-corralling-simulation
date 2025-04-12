import numpy as np

N = 13
target = (7, 7)
obstacles = {(6,6), (6,7), (6,8), (7,6), (8,6), (8,7), (8,8)}
epsilon = 0.01  


T_star = {}
for xB in range(N):
    for yB in range(N):
        for xC in range(N):
            for yC in range(N):
                T_star[((xB, yB), (xC, yC))] = float('inf')
                if (xB, yB) == target:
                    T_star[((xB, yB), (xC, yC))] = 0  


startB = (1, 12)  
startC = (12, 0)  


def get_robot_moves(posC):
    
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return [(posC[0] + dx, posC[1] + dy) for dx, dy in moves if is_valid((posC[0] + dx, posC[1] + dy))]

def get_bull_moves(posB, posC):
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bull_moves = [(posB[0] + dx, posB[1] + dy) for dx, dy in moves if is_valid((posB[0] + dx, posB[1] + dy))]
    
    if manhattan(posB, posC) <= 2:
        bull_moves = [m for m in bull_moves if manhattan(m, posC) <= manhattan(posB, posC)]
    
    if not bull_moves:
        bull_moves = [posB]
    return bull_moves

def is_valid(pos):
    
    return 0 <= pos[0] < N and 0 <= pos[1] < N and pos not in obstacles

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def compute_T_star():
    max_diff = float('inf')
    while max_diff > epsilon:
        max_diff = 0  
        for posB in [(x, y) for x in range(N) for y in range(N) if (x, y) != target]:
            for posC in [(x, y) for x in range(N) for y in range(N)]:
                if posB == target:
                    continue
                min_rounds = float('inf')
                for c in get_robot_moves(posC):
                    bull_moves = get_bull_moves(posB, c)
                    expected_value = sum(T_star[(b, c)] for b in bull_moves) / len(bull_moves)
                    min_rounds = min(min_rounds, 1 + expected_value)
                
                old_value = T_star[(posB, posC)]
                T_star[(posB, posC)] = min_rounds
                max_diff = max(max_diff, abs(old_value - min_rounds))  


compute_T_star()


expected_time = T_star.get((startB, startC), float('inf'))


if expected_time < float('inf'):
    print("Yes, the robot can pen the bull in an expected time of {:.2f} rounds.".format(expected_time))
else:
    print("No, the robot cannot pen the bull in a finite expected time from the initial positions.")
