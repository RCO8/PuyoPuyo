#필수 초기화
import pygame
import random
import bg_colors
from resources import ImageResources, BackgoundMusic

pygame.init()

#화면 크기
screen = pygame.display.set_mode((304,512))

#아이콘 설정

icon = ImageResources('icon.png')
pygame.display.set_icon(icon.sprite)

#FPS
clock = pygame.time.Clock()

#화면 타이틀
pygame.display.set_caption("뿌요뿌요")

#게임 폰트
game_font = pygame.font.Font(None, 40)

#게임 배경 및 이미지

red = ImageResources('red.png')
red.setPosition(0,0)
red.setClipping(0,0,16,16)

yellow = ImageResources('yellow.png')
yellow.setPosition(16,0)
yellow.setClipping(0,0,16,16)

green = ImageResources('green.png')
green.setPosition(32,0)
green.setClipping(0,0,16,16)

blue = ImageResources('blue.png')
blue.setPosition(48,0)
blue.setClipping(0,0,16,16)

purple = ImageResources('purple.png')
purple.setPosition(64,0)
purple.setClipping(0,0,16,16)

#데이터 설정
puyoBottle = []    #기본 틀 만들기 {1:red, 2:yellow, 3:green, 4:blue, 5:purple}
for i in range(20):
    tmp = []
    for j in range(10):
        tmp.append(0)
    puyoBottle.append(tmp)

#움직일 블록
roundDrops = [[0,0,0],[0,0,0],[0,0,0]]
roundDrops[0][1] = random.randrange(1,6)
roundDrops[1][1] = random.randrange(1,6)
roundMoves = 0
roundDropsX = 0
roundDropsY = 0

#이미지 그리기
def drawImage():
    screen.fill(bg_colors.bg_black)
    
    #기본틀
    for i in range(19,-1,-1):
        for j in range(9,-1,-1):
            if(puyoBottle[i][j] == 1):
                screen.blit(red.sprite, (j*16,i*16), red.sprite_clip)
            elif(puyoBottle[i][j] == 2):
                screen.blit(yellow.sprite, (j*16,i*16),yellow.sprite_clip)
            elif(puyoBottle[i][j] == 3):
                screen.blit(green.sprite, (j*16,i*16),green.sprite_clip)
            elif(puyoBottle[i][j] == 4):
                screen.blit(blue.sprite, (j*16,i*16),blue.sprite_clip)
            elif(puyoBottle[i][j] == 5):
                screen.blit(purple.sprite, (j*16,i*16),purple.sprite_clip)
    
    #블록
    for i in range(0,3):
        for j in range(0,3):
            if(roundDrops[i][j] == 1):
                screen.blit(red.sprite, ((j+roundDropsX)*16,i*16), red.sprite_clip)
            elif(roundDrops[i][j] == 2):
                screen.blit(yellow.sprite, ((j+roundDropsX)*16,i*16),yellow.sprite_clip)
            elif(roundDrops[i][j] == 3):
                screen.blit(green.sprite, ((j+roundDropsX)*16,i*16),green.sprite_clip)
            elif(roundDrops[i][j] == 4):
                screen.blit(blue.sprite, ((j+roundDropsX)*16,i*16),blue.sprite_clip)
            elif(roundDrops[i][j] == 5):
                screen.blit(purple.sprite, ((j+roundDropsX)*16,i*16),purple.sprite_clip)
    

#게임 진행 루프
running = True
while running:
    #초당 지정된 프레임 횟수동안 동작
    dt = clock.tick(10)

    set_speed = 3
    #키보드 이벤트
    for event in pygame.event.get():
        #화면 창을 닫을 때
        if event.type == pygame.QUIT:
            running = False
        #키를 누르고 있을 때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("좌로 이동")
                roundMoves = -1
            elif event.key == pygame.K_RIGHT:
                print("우로 이동")
                roundMoves = 1
            if event.key == pygame.K_UP:
                print("바로 내리기")
            elif event.key == pygame.K_DOWN:
                print("더 내리기")
            if event.key == pygame.K_z:
                #print("좌로 회전")
                if roundDrops[0][1] > 0:
                    roundDrops[1][0] = roundDrops[0][1]
                    roundDrops[0][1] = 0
                elif roundDrops[1][0] > 0:
                    roundDrops[2][1] = roundDrops[1][0]
                    roundDrops[1][0] = 0
                elif roundDrops[2][1] > 0:
                    roundDrops[1][2] = roundDrops[2][1]
                    roundDrops[2][1] = 0
                elif roundDrops[1][2] > 0:
                    roundDrops[0][1] = roundDrops[1][2]
                    roundDrops[1][2] = 0 
            elif event.key == pygame.K_x:
                #print("우로 회전")
                if roundDrops[0][1] > 0:
                    roundDrops[1][2] = roundDrops[0][1]
                    roundDrops[0][1] = 0
                elif roundDrops[1][2] > 0:
                    roundDrops[2][1] = roundDrops[1][2]
                    roundDrops[1][2] = 0
                elif roundDrops[2][1] > 0:
                    roundDrops[1][0] = roundDrops[2][1]
                    roundDrops[2][1] = 0
                elif roundDrops[1][0] > 0:
                    roundDrops[0][1] = roundDrops[1][0]
                    roundDrops[1][0] = 0 
        #키를 떼었을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                roundMoves = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ypos = 0
    
    #갱신
    roundDropsX += roundMoves
    drawImage()
    
    pygame.display.update()

pygame.time.delay(500)
pygame.quit()