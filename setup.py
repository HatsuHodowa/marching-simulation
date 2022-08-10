import time
import sys
import os
import threading
from perlin_noise import PerlinNoise

import pygame
pygame.init()

sys.path.append("shapes")
sys.path.append("render")
sys.path.append("services")
sys.path.append("terrain")
sys.path.append("car_stuff")
sys.path.append("user_interface")
sys.path.append("marching")

from polygon import *
from regular_polygons import *
from circle import *
from rect import *
from image_rect import *
from line import *

from camera import *

from tagservice import *

from gui_object import *
from frame import *
from text_label import *
from text_box import *

from band_member import *
from squad import *
from metronome import *

# creating clock
clock = pygame.time.Clock()

# creating window
screen = pygame.display.set_mode((1000, 600))#, pygame.FULLSCREEN, pygame.RESIZABLE)
pygame.display.set_caption("marching simulation")
screen_open = True
last_time = time.time()

# creating main camera
camera = Camera(surface=screen)
Tag.add_tag(screen, camera)

# running scripts
on_run = "on_run"
for file_name in os.listdir(on_run):
    f = os.path.join(on_run, file_name)
    if os.path.isfile(f):
        py = open(f, "r")
        def ex(py):
            exec(py.read())

        # running thread
        thread = threading.Thread(target=ex, name=file_name, args=[py])
        thread.start()
        
while screen_open == True:
    
    # max framerate
    clock.tick(30)

    # calculating dt
    dt = time.time() - last_time
    last_time = time.time()

    # handing camera targets
    camera.lock_on_target()

    # running input
    input_f = "render/input.py"
    input_py = open(input_f, "r")
    exec(input_py.read())

    # handling pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_open = False
        elif event.type == pygame.MOUSEBUTTONDOWN and camera.movement_enabled:
            if event.button == 4:
                camera.zoom = min(camera.zoom + camera.zoomspeed, camera.zoom_max)
            elif event.button == 5:
                camera.zoom = max(camera.zoom - camera.zoomspeed, camera.zoom_min)

        # text boxes
        for box in TextBox.all_texts:
            box.process_event(event)

    # fill a white background
    screen.fill((0, 150, 0))

    # drawing all polygons & updating physics
    for poly in Polygon.get_surface_polygons(screen):
        poly.update_physics(dt)
        poly.draw()

    # drawing user interface
    for ui_obj in GUIObject.all_uis:
        ui_obj.render_ui()

    # update the display
    pygame.display.flip()

pygame.quit()