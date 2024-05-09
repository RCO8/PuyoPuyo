board = []  # [1:red, 2:yellow, 3:green, 4:blue, 5:purple]

#게임 초기함수
def dataInit():
    #10x20의 사이즈 뿌요판 설정
    for i in range(20):
        tmp = []
        for j in range(10):
            tmp.append(0)
        board.append(tmp)
    return

#각 블록 제어
def RotateBlock(x, y, dir = 0):
    if dir < 0: #좌로 회전
        if board[y - 1][x] > 0: #위에 블록이 있으면
            board[y][x - 1] = board[y - 1][x]
            board[y - 1][x] = 0
        elif board[y][x - 1] > 0: #왼쪽에 블록이 있으면
            board[y + 1][x] = board[y][x - 1];
            board[y][x - 1] = 0
        elif board[y + 1][x] > 0: #아래에 블록이 있으면
            board[y][x + 1] = board[y + 1][x]
            board[y + 1][x] = 0
        elif board[y][x + 1] > 0: #오른쪽에 블록이 있으면
            board[y - 1][x] = board[y][x + 1]
            board[y][x + 1] = 0
    elif dir > 0: #우로 회전
        if board[y - 1][x] > 0: #위에 블록이 있으면
            board[y][x + 1] = board[y - 1][x]
            board[y - 1][x] = 0
        elif board[y][x + 1] > 0: #오른쪽에 블록이 있으면
            board[y + 1][x] = board[y][x + 1]
            board[y][x + 1] = 0
        elif board[y + 1][x] > 0: #아래에 블록이 있으면
            board[y][x - 1] = board[y + 1][x]
            board[y + 1][x] = 0
        elif board[y][x - 1] > 0: #왼쪽에 블록이 있으면
            board[y - 1][x] = board[y][x - 1]
            board[y][x - 1] = 0
    return
def MoveBlock(blocks, direction):
    #Point Block
    blocks[0][0] += direction
    board[blocks[0][1]][blocks[0][0]] = blocks[0][2]
    board[blocks[0][1]][blocks[0][0] - direction] = 0
    #Rotate Block
    blocks[1][0] += direction
    board[blocks[1][1]][blocks[1][0]] = blocks[1][2]
    board[blocks[1][1]][blocks[1][0] - direction] = 0
    return

#블록 판정

def DownBlock(blocks):
    #Point Block
    blocks[0][1] += 1
    board[blocks[0][1]][blocks[0][0]] = blocks[0][2]
    #Rotate Block
    blocks[1][1] += 1
    board[blocks[1][1]][blocks[1][0]] = blocks[1][2]
    board[blocks[1][1]-1][blocks[1][0]] = 0