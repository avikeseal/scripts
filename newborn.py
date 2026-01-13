#!usr/bin/env bash python3

import pygame 
import math
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#screen dimensions:
WIDTH, HEIGHT = 1300, 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GRAVITY SIMULATION")

#initializing pygame:
pygame.init()

#game loop variable:
running = True

#main game loop:
while running:
	#A. handle events such as mouse clicks, keyboard press, widndow close etc)
	for event in pygame.event.get():
