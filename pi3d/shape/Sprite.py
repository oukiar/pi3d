from pi3d import *
from pi3d import Texture
from pi3d.Buffer import Buffer
from pi3d.shape.Shape import Shape

class Sprite(Shape):
  def __init__(self, camera, light, w=1.0, h=1.0, name="",
               x=0.0, y=0.0, z=10.0,
               rx=0.0, ry=0.0, rz=0.0,
               sx=1.0, sy=1.0, sz=1.0,
               cx=0.0, cy=0.0, cz=0.0):
    super(Sprite, self).__init__(camera, light, name, x, y, z, rx, ry, rz,
                                sx, sy, sz, cx, cy, cz)

    if VERBOSE:
      print "Creating sprite ..."

    self.width = w
    self.height = h
    self.ttype = GL_TRIANGLES
    self.verts = []
    self.norms = []
    self.texcoords = []
    self.inds = []

    ww = w / 2.0
    hh = h / 2.0

    self.verts = ((-ww, hh, z), (ww, hh, z), (ww, -hh, z), (-ww,-hh, z))
    self.norms = ((0, 0, -1), (0, 0, -1),  (0, 0, -1), (0, 0, -1))
    self.texcoords = ((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0 ,1.0))

    self.inds = ((0, 1, 3), (1, 2, 3))
    
    self.buf = []
    self.buf.append(Buffer(self, self.verts, self.texcoords, self.inds, self.norms))