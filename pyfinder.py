import pygame
import cv2
from hs import *
WINDOW_WIDTH = int(1.5 * 812)
WINDOW_HEIGHT = int(1.5* 531)
TOTAL_ROWS = 265
TOTAL_COLS = 406
def main():
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("A* Path Finding Algorithm")
    #replace with you file path the image
    image = cv2.imread(r'D:\educational\projects\Graduation Project\pyfinder\edited.png')
    grid = make_grid(TOTAL_COLS,TOTAL_ROWS,WINDOW_WIDTH,WINDOW_HEIGHT,image)
    py_game_running = True
    start = None
    destination = None
    while py_game_running:
        draw(window,grid,TOTAL_ROWS,TOTAL_COLS,WINDOW_WIDTH,WINDOW_HEIGHT)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                py_game_running = False
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = get_clicked_pos(position,TOTAL_ROWS,TOTAL_COLS,WINDOW_WIDTH,WINDOW_HEIGHT)
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
                    path_list = astar(start,destination,grid,TOTAL_ROWS,TOTAL_COLS)


                    print(path_list)


if "__main__" in __name__:
    main()