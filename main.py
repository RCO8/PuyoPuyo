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
puyoBottle = [[0] * 10] * 20    #기본 틀 만들기 {1:red, 2:yellow, 3:green, 4:blue, 5:purple}
#print(puyoBottle)

#이미지 그리기
def drawImage():
    screen.fill(bg_colors.bg_black)
    screen.blit(red.sprite, red.getPosition(), red.sprite_clip)
    screen.blit(yellow.sprite,yellow.getPosition(),yellow.sprite_clip)
    screen.blit(green.sprite,green.getPosition(),green.sprite_clip)
    screen.blit(blue.sprite,blue.getPosition(),blue.sprite_clip)
    screen.blit(purple.sprite,purple.getPosition(),purple.sprite_clip)

#게임 진행 루프
running = True
while running:
    #초당 지정된 프레임 횟수동안 동작
    dt = clock.tick(60)

    set_speed = 3
    #키보드 이벤트
    for event in pygame.event.get():
        #화면 창을 닫을 때
        if event.type == pygame.QUIT:
            running = False
        #키를 누르고 있을 때
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xpos -= set_speed
            elif event.key == pygame.K_RIGHT:
                xpos += set_speed
            if event.key == pygame.K_UP:
                ypos -= set_speed
            elif event.key == pygame.K_DOWN:
                ypos += set_speed
        #키를 떼었을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xpos = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ypos = 0
        #마우스 체크
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
        
    drawImage()
    #갱신
    pygame.display.update()

pygame.time.delay(500)
pygame.quit()