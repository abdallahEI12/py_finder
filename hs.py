import cv2
from random import randint
from queue import PriorityQueue
import pygame

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
class Sf():
    def __init__(self):
        self.frntr = []

    def add(self, nd):
        self.frntr.append(nd)

    def contains_stt(self, stt):
        return any(nd.stt == stt for nd in self.frntr)

    def empty(self):
        return len(self.frntr) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frntr")
        else:
            nd = self.frntr[-1]
            self.frntr = self.frntr[:-1]
            return nd

class Nd:
    def __init__(self,r,c,w,h,clr_image):
        self.r = r
        self.c = c
        self.stt = (self.r,self.c)
        self.w = w
        self.h = h
        self.clr = tuple(clr_image[c][r])[::-1]
        self.x = r * w
        self.y = c * w
        self.p = None
        self.h_c = None
        self.g_c = None
        self.number = None
        self.start = False
        self.end = False

    def draw(self, win):
        pygame.draw.rect(win, self.clr, (self.x, self.y, self.w, self.h))

    def get_pos(self):
        return self.r, self.c

def get_clicked_pos(mouse_pos, ttl_r,ttl_c, w_w,w_h):
    h_gap = w_w // ttl_c
    v_gap = w_h // ttl_r
    y, x = mouse_pos

    r = y // v_gap
    c = x // h_gap

    return r, c

def make_grid(ttl_r,ttl_cs, w_w,w_h,clr_iamge):
    grid =[]

    nd_w = w_w//ttl_r
    nd_h = w_h // ttl_cs
    for i in range(ttl_r):
        grid.append([])
        for j in range(ttl_cs):
            nd = Nd(i,j,nd_w,nd_h,clr_iamge)
            grid[i].append(nd)
    return grid

def draw_grid(window, ttl_r, ttl_cs, w_w,w_h):

    h_gap = w_w // ttl_cs
    v_gap = w_h // ttl_r
    for i in range(ttl_r):
        pygame.draw.line(window, GREY, (0, i * h_gap), (w_w, i * h_gap))
        for j in range(ttl_cs  ):
            pygame.draw.line(window, GREY, (j * v_gap, 0), (j * v_gap, w_w))

def draw(window, grid,ttl_r,ttl_cs,w_w,w_h):
    window.fill(WHITE)

    for r in grid:
        for nd in r:
            nd.draw(window)

    pygame.display.update()



def astar(start,end,maze,ttl_r,ttl_cs):
    num_explored = 0
    start.number = 0
    start.g_c = 0
    start.h_c = h(start,end)
    frntr = Sf()

    frntr.add(start)

    explored = set()

    while True:
        if frntr.empty():
            raise Exception('no solution')

        nd = frntr.remove()
        nd.clr=RED
        num_explored+=1

        if nd.stt == end.stt:
            path = []
            while nd.p is not None:
                path.append(nd)
                nd=nd.p
            path.reverse()
            return path

        explored.add(nd)

        nbrs = get_nbrs(nd,maze,ttl_r,ttl_cs)


        for nbr in nbrs:
            nbr.p = nd
            nbr.h_c = h(nbr,end)
            nbr.g_c = nbr.p.g_c + 1


        for nbr in sorted(nbrs,key= lambda x : (x.h_c + x.g_c),reverse=True):

            if not frntr.contains_stt(nbr.stt) and nbr not in explored:
                frntr.add(nbr)


def h(nd, end_nd):
    x2,y2 = end_nd.stt
    x1,y1 = nd.stt
    return abs(y2-y1) + abs(x2-x1)


def get_nbrs(nd,maze,ttl_r, ttl_cs):
    r,c =nd.stt
    candidates = [
        (r - 1, c),
        (r + 1, c),
        (r, c - 1),
        (r, c + 1)
    ]
    nbrs = []

    for r,c in candidates:
        nbr = maze[r][c]
        nbr_clr = nbr.clr
        if 0 <= r < ttl_cs and 0 <= c < ttl_r and (nbr_clr== (255,255,128) or nbr_clr == BLUE):
            nbr = nbr
            nbrs.append(nbr)
    return nbrs
