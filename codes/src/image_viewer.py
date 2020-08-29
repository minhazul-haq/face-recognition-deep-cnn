from PIL import Image, ImageTk

class DisplayGraphics:
    def __init__(self, root, master, image_filename, objects=[]):
        self.root = root
        self.master = master
        self.filename = image_filename
        self.objects = objects
        self.canvas=self.master.canvas
        self.canvas.config(width=600, height = 400)
        #self.show_image(image_filename)

    def show_image(self, image_filename):
        img = Image.open(image_filename)
        filename = ImageTk.PhotoImage(img)
        self.canvas.image = filename
        self.canvas.create_image(0, 0, anchor='nw', image=filename)
        #self.canvas.pack()

    def create_graphic_objects(self):
        self.objects.append(self.canvas.create_oval(int(0.25 * int(self.canvas.cget("width"))),
                                               int(0.25 * int(self.canvas.cget("height"))),
                                               int(0.75 * int(self.canvas.cget("width"))),
                                               int(0.75 * int(self.canvas.cget("height")))))
        self.objects.append(self.canvas.create_oval(int(0.30 * int(self.canvas.cget("width"))),
                                               int(0.30 * int(self.canvas.cget("height"))),
                                               int(0.70 * int(self.canvas.cget("width"))),
                                               int(0.70 * int(self.canvas.cget("height")))))
        self.objects.append(self.canvas.create_oval(int(0.35 * int(self.canvas.cget("width"))),
                                               int(0.35 * int(self.canvas.cget("height"))),
                                               int(0.65 * int(self.canvas.cget("width"))),
                                               int(0.65 * int(self.canvas.cget("height")))))

    def draw_bounding_box(self, bb):
        self.objects.append(self.canvas.create_rectangle(bb[0], bb[1], bb[2], bb[3]))

    def redisplay(self, event):
        if self.objects:
            self.canvas.coords(self.objects[0], int(0.25 * int(event.width)),
                          int(0.25 * int(event.height)),
                          int(0.75 * int(event.width)),
                          int(0.75 * int(event.height)))
            self.canvas.coords(self.objects[1], int(0.30 * int(event.width)),
                          int(0.30 * int(event.height)),
                          int(0.70 * int(event.width)),
                          int(0.70 * int(event.height)))
            self.canvas.coords(self.objects[2], int(0.35 * int(event.width)),
                          int(0.35 * int(event.height)),
                          int(0.65 * int(event.width)),
                          int(0.65 * int(event.height)))
