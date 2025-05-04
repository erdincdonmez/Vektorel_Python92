import curses
import random
import time

shapes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if (y + off_y >= len(board) or
                    x + off_x < 0 or
                    x + off_x >= len(board[0]) or
                    board[y + off_y][x + off_x]):
                    return True
    return False

def merge(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = cell

def clear_rows(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    rows_cleared = len(board) - len(new_board)
    return [[0] * len(board[0]) for _ in range(rows_cleared)] + new_board

def draw_board(stdscr, board, score):
    stdscr.clear()
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            char = "#" if cell else "."
            stdscr.addstr(y, x * 2, char * 2)
    stdscr.addstr(len(board), 0, f"Score: {score}")
    stdscr.refresh()

def tetris(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    height, width = 20, 10
    board = [[0 for _ in range(width)] for _ in range(height)]
    score = 0

    shape = random.choice(shapes)
    pos = [width // 2 - len(shape[0]) // 2, 0]

    tick = time.time()

    while True:
        now = time.time()
        if now - tick > 0.5:
            if not check_collision(board, shape, [pos[0], pos[1] + 1]):
                pos[1] += 1
            else:
                merge(board, shape, pos)
                board = clear_rows(board)
                shape = random.choice(shapes)
                pos = [width // 2 - len(shape[0]) // 2, 0]
                if check_collision(board, shape, pos):
                    stdscr.addstr(22, 0, "GAME OVER")
                    stdscr.refresh()
                    time.sleep(2)
                    break
            tick = now

        try:
            key = stdscr.getkey()
            if key == 'a' and not check_collision(board, shape, [pos[0] - 1, pos[1]]):
                pos[0] -= 1
            elif key == 'd' and not check_collision(board, shape, [pos[0] + 1, pos[1]]):
                pos[0] += 1
            elif key == 's' and not check_collision(board, shape, [pos[0], pos[1] + 1]):
                pos[1] += 1
            elif key == 'w':
                new_shape = rotate(shape)
                if not check_collision(board, new_shape, pos):
                    shape = new_shape
        except:
            pass

        temp_board = [row[:] for row in board]
        merge(temp_board, shape, pos)
        draw_board(stdscr, temp_board, score)

curses.wrapper(tetris)
