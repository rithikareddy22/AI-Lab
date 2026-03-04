import time
from collections import deque


TOTAL_M = 3
TOTAL_C = 3

def is_valid(state):
    M_left, C_left, boat = state
    M_right = TOTAL_M - M_left
    C_right = TOTAL_C - C_left

    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False

    if (M_left > 0 and C_left > M_left):
        return False

    if (M_right > 0 and C_right > M_right):
        return False

    return True


def get_successors(state):
    M_left, C_left, boat = state
    successors = []

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for m, c in moves:
        if boat == 0:  
            new_state = (M_left - m, C_left - c, 1)
        else:  
            new_state = (M_left + m, C_left + c, 0)

        if is_valid(new_state):
            successors.append(new_state)

    return successors


def bfs(start, goal):
    start_time = time.time()
    queue = deque([[start]])
    visited = set()
    nodes = 0

    while queue:
        path = queue.popleft()
        state = path[-1]
        nodes += 1

        if state == goal:
            return path, nodes, time.time() - start_time

        if state not in visited:
            visited.add(state)

            for child in get_successors(state):
                new_path = list(path)
                new_path.append(child)
                queue.append(new_path)

    return None, nodes, time.time() - start_time

def dfs(start, goal):
    start_time = time.time()
    stack = [[start]]
    visited = set()
    nodes = 0

    while stack:
        path = stack.pop()
        state = path[-1]
        nodes += 1

        if state == goal:
            return path, nodes, time.time() - start_time

        if state not in visited:
            visited.add(state)

            for child in get_successors(state):
                new_path = list(path)
                new_path.append(child)
                stack.append(new_path)

    return None, nodes, time.time() - start_time


def dls(start, goal, limit):
    start_time = time.time()
    stack = [(start, [start], 0)]
    nodes = 0

    while stack:
        state, path, depth = stack.pop()
        nodes += 1

        if state == goal:
            return path, nodes, time.time() - start_time

        if depth < limit:
            for child in get_successors(state):
                stack.append((child, path + [child], depth + 1))

    return None, nodes, time.time() - start_time

def iddfs(start, goal, max_depth=20):
    start_time = time.time()
    total_nodes = 0

    for depth in range(max_depth):
        result, nodes, _ = dls(start, goal, depth)
        total_nodes += nodes

        if result:
            return result, total_nodes, time.time() - start_time

    return None, total_nodes, time.time() - start_time

if __name__ == "__main__":

    start_state = (3, 3, 0)
    goal_state = (0, 0, 1)

    print("\n===== BFS =====")
    path, nodes, t = bfs(start_state, goal_state)
    print("Path:", path)
    print("Nodes Expanded:", nodes)
    print("Time:", t)

    print("\n===== DFS =====")
    path, nodes, t = dfs(start_state, goal_state)
    print("Path:", path)
    print("Nodes Expanded:", nodes)
    print("Time:", t)

    print("\n===== DLS (limit=20) =====")
    path, nodes, t = dls(start_state, goal_state, 20)
    print("Path:", path)
    print("Nodes Expanded:", nodes)
    print("Time:", t)

    print("\n===== IDDFS =====")
    path, nodes, t = iddfs(start_state, goal_state)
    print("Path:", path)
    print("Nodes Expanded:", nodes)
    print("Time:", t)