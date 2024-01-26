import pygame
import cv2
from hs import *
WW = int(1.5 * 812)
WH = int(1.5* 531)
TTL_R = 265
TTL_C = 406
def main():
    window = pygame.display.set_mode((WW,WH))
    pygame.display.set_caption("A* Path Finding Algorithm")
    #replace with you file path the image
    image = cv2.imread(r'D:\educational\projects\Graduation Project\pyfinder\edited.png')
    grid = make_grid(TTL_C,TTL_R,WW,WH,image)
    py_game_running = True
    start = None
    destination = None
    while py_game_running:
        draw(window,grid,TTL_R,TTL_C,WW,WH)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                py_game_running = False
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = get_clicked_pos(position,TTL_R,TTL_C,WW,WH)
                pressed_node = grid[row][col]
                if not start and pressed_node != destination:
                    pressed_node.start = True
                    start = pressed_node
                    pressed_node.clr = RED
                elif not destination and pressed_node != start:
                    pressed_node.end = True
                    destination = pressed_node
                    pressed_node.clr = BLUE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and destination:
                    path_list = astar(start,destination,grid,TTL_R,TTL_C)


                    print(path_list)


if "__main__" in __name__:
    main()