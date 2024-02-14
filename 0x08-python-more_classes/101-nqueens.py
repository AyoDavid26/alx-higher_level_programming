#!/usr/bin/python3
"""Solution to the nqueen puzzle.

to determine all possible solutionto placing N.
where N is non-attacking queen on an NxN chessboard.

N must be an integer that is greater than or equal to 4.

where:
    board (list) : List of lists represening the chessboard
    solution (list) : List of solution containing list.

solution representation are in format: [[r, c], [r, c], [r, c], [r, c]].
'r' represents rows
'c' represents columns where a queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """initializing an 'N' x 'N' sized chessboard with 0's."""

    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """To return a deepcopy of the chessboard"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """X spots on a chessboard.

    all spots where non-attacking queens can not be played are
    marked X.

    where:
    board(list): Current working chessboard.
    row(int): Last row where a queen was played
    col(int): Last column where a queen was played.
    """
    # X out all the forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = 'x'
    # X out all the backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all the spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all the spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all the spots diagonally down the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all the spots diagonally up the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all the spots diagonally down the left
    c = col - 1
    for r in range(ro + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    # X out all the spots diagonally up the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1


def recusive_solve(board, row, queens, solutions):
    """ Solving an N-queens puzzle recursivelyy.

    where:
        board (list): Current working chessboard.
        row (int): Current working row.
        queens (int): Current number of placed queens.
        solutions (list): List of solutions list.
    Returns:
        Solutions.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + solutions)

        return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
