""" GPU doing conways game of life. ESC to quit
this shows how it is possible to recycle images from the renderbuffer
and use the very fast processing speed of the GPU to do certain tasks.
"""
import ctypes
import demo
import pi3d
from pi3d.constants import *

WIDTH = 800
HEIGHT = 800
DISPLAY = pi3d.Display.create(w=WIDTH, h=HEIGHT)
CAMERA = pi3d.Camera(is_3d=False)
shader = pi3d.Shader("shaders/conway")

tex = []
tex.append(pi3d.Texture("textures/Roof.png", mipmap=False))
tex.append(pi3d.Texture("textures/Roof.png", mipmap=False))
sprite = pi3d.Sprite(camera=CAMERA, w=WIDTH, h=HEIGHT, x=0.0, y=0.0, z=1.0)
sprite.set_draw_details(shader, [tex[0]])
sprite.set_2d_size(WIDTH, HEIGHT, 0.0, 0.0) # used to get pixel scale by shader

ti = 0 # variable to toggle between two textures
img = (ctypes.c_char * (WIDTH * HEIGHT * 3))() # to hold pixels
mykeys = pi3d.Keyboard()

while DISPLAY.loop_running():
  sprite.draw()
  
  ti = (ti+1) % 2
  pi3d.opengles.glReadPixels(0, 0, WIDTH, HEIGHT, GL_RGB, GL_UNSIGNED_BYTE,
                        ctypes.byref(img))
  pi3d.opengles.glBindTexture(GL_TEXTURE_2D, tex[ti]._tex)
  opengles.glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, WIDTH, HEIGHT, 0, GL_RGB,
                        GL_UNSIGNED_BYTE, img)
  sprite.set_draw_details(shader, [tex[ti]])

  if mykeys.read() == 27:
    mykeys.close()
    DISPLAY.destroy()
    break
