# ........
# ........
# ..*.....
# ........
# ........
# .....**.
# ...*....
# ........

ans = 0
cols = [False] * 8
first_diagonal, second_diagonal = [False] * 15, [False] * 15
board = [[x for x in input()] for _ in range(8)]

def solution(row):
    global ans, cols, first_diagonal, second_diagonal, board
    if row == 8:
        ans += 1
        return
    
    for c in range(8):
        if cols[c] or first_diagonal[row + c] or second_diagonal[c - row + 7] or board[row][c] == "*":
            continue
        cols[c] = first_diagonal[row + c] = second_diagonal[c - row + 7] = True
        solution(row + 1)
        cols[c] = first_diagonal[row + c] = second_diagonal[c - row + 7] = False

solution(0)
print(ans)