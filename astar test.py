import pygame
import Movement

# test to see if I can f**king commit!!!!

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("A-star")

clock = pygame.time.Clock()
clock.tick(60)
run = True

startPos = (0, 0)
endPos = (9, 9)
mPos = (0, 0)
Path = []
atEnd = False
curnode = startPos
move = Movement.pathFind()

Map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

while run:
    screen.fill((255, 255, 255))

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.mouse.get_pressed()[0]:
        mpos = pygame.mouse.get_pos()
        Map[int(mpos[0] / 70)][int(mpos[1] / 70)] = 1

    if pygame.mouse.get_pressed()[2]:
        mpos = pygame.mouse.get_pos()
        Map[int(mpos[0] / 70)][int(mpos[1] / 70)] = 0

    #-DRAW GRID-#
    for x in range(10):
        pygame.draw.line(screen, (0, 0, 0), (x * 70, 0), (x * 70, 700), 3) # Vertical lines
        for y in range(10):
            pygame.draw.line(screen, (0, 0, 0), (0, y * 70), (700, y * 70), 3) # Horisontal lines

            #-COLORING IN FUNCTION-#
            if Map[x][y] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (x * 70, y * 70, 70, 70))

    # if curnode != endPos:
    if key[pygame.K_SPACE]:
        Path = move.aStar(Map, startPos, endPos)

    # print("path: " + str(path))

    #-DRAW THE PATH-#
    for i in Path:
        pygame.draw.rect(screen, (0, 255, 0), (i[0] * 70, i[1] * 70, 70, 70))

    pygame.display.flip()
pygame.quit()