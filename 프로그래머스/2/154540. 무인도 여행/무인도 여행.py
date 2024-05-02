import sys
sys.setrecursionlimit(10000)

def update_island(island, i, j):
    if i not in island:
        island[i] = set()
    island[i].add(j)

def sum_food(maps, x, y, island):
    sum = int(maps[x][y])
    update_island(island, x, y)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and ny not in island.get(nx, set()):
            sum += sum_food(maps, nx, ny, island)
    return sum

def solution(maps):
    islands = {}
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and j not in islands.get(i, set()):
                food = sum_food(maps, i, j, islands)
                answer.append(food)
    if answer:
        return sorted(answer)

    return [-1]
