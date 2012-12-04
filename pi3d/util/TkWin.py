from Tkinter import Tk

class TkWin(Tk):
  def __init__(self, parent, title,width,height):
    Tk.__init__(self, parent)

    def mouseclick_callback(event):
      if not self.resized:
        self.ev = 'click'
        self.x = event.x
        self.y = event.y

    def mousemove_callback(event):
      if not self.resized:
        self.ev = 'move'
        self.x = event.x
        self.y = event.y

    def mousewheel_callback(event):
      if not self.resized:
        self.ev = 'wheel'
        self.num = event.num
        self.delta = event.delta

    def drag_callback(event):
      if not self.resized:
        self.ev = 'drag'
        self.x = event.x
        self.y = event.y
        mouserot = event.x

    def resize_callback(event):
      self.ev = 'resized'
      self.winx = self.winfo_x()
      self.winy = self.winfo_y()
      self.width = event.width
      self.height = event.height
      self.resized = True

    def key_callback(event):
      if not self.resized:
        self.ev = 'key'
        self.key = event.keysym
        self.char = event.char

    Tk.bind(self, '<Button-1>', mouseclick_callback)
    Tk.bind(self, '<B1-Motion>', drag_callback)
    Tk.bind(self, '<Motion>', mousemove_callback)
    Tk.bind(self, '<MouseWheel>', mousewheel_callback)
    Tk.bind(self, '<Configure>', resize_callback)
    Tk.bind_all(self, '<Key>', key_callback)
    Tk.geometry(self, str(width) + 'x' + str(height))

    self.title(title)
    self.ev = ''
    self.resized = False

