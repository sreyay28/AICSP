
def check_pos(board, size, row, col):

    for i in range(size):
        if board[row][i] == 1:
            return False

    x, y = row, col
    while x >= 0 and y >= 0:
        if board[x][y] == 1:
            return False
        x -= 1
        y -= 1

    x, y = row, col
    while x < size and y >= 0:
        if board[x][y] == 1:
            return False
        x += 1
        y -= 1

    return True

def backtracking_search(board, size):
    return recursive_backtracking(board, size, 0)

def recursive_backtracking(board, size, col):

    if isComplete(board, size):
        return board

    for i in range(size):
        bool = check_pos(board, size, i, col)
        if(bool):
            board[i][col] = 1
            result = recursive_backtracking(board, size, col+1)
            if(result == None):
                board[i][col] = 0
            else:
                return result
    return None

# driver program to test above function
def isComplete(board, size):
    count = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == 1:
                count += 1
    if count == size:
        return True
    return False

def main():
    size = input("Enter the size: ")

    w = int(size)
    board = [[0 for x in range(w)] for y in range(w)]
    result = backtracking_search(board, int(size))

    for i in range(int(size)):
        for j in range(int(size)):
            print(result[i][j], end = " ")
        print()

if __name__ == '__main__':
    main()