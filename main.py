#필수 초기화
import pygame
import random
import bg_colors
from resources import ImageResources, BackgoundMusic
import dataInit

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
green.setClipping(0,0,16,16)

blue = ImageResources('blue.png')
blue.setPosition(48,0)
blue.setClipping(0,0,16,16)

purple = ImageResources('purple.png')
purple.setPosition(64,0)
purple.setClipping(0,0,16,16)

#데이터 설정
dataInit.dataInit()

#움직일 블록

#이미지 그리기
def drawImage():
    screen.fill(bg_colors.bg_black)
    screen.fill(bg_colors.bg_orange,(0,0,160,320))  #블록판 채우기


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
                #print("좌로 이동")
                roundMoves = -1
            elif event.key == pygame.K_RIGHT:
                #print("우로 이동")
                roundMoves = 1
            if event.key == pygame.K_UP:
                print("바로 내리기")
            elif event.key == pygame.K_DOWN:
                #print("더 내리기")
                roundDown = True
            if event.key == pygame.K_z:
                print("좌로 회전")
            elif event.key == pygame.K_x:
                print("우로 회전")
        #키를 떼었을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                roundMoves = 0
            if event.key == pygame.K_DOWN:
                roundDown = False
    
    #갱신
        
    #판정
    pygame.display.update()
        
    drawImage()
    

pygame.time.delay(500)
pygame.quit()