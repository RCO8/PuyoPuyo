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
def blockControl():
    #중심 블록
    #회전 블록

    return