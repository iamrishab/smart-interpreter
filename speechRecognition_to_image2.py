import tkinter as tk
import glob
import os
from PIL import Image, ImageTk

def messageWindow():
    win = tk.Toplevel()
    path = r'/Users/rishabpal/PycharmProjects/untitled/saved_images/'
    COLUMNS = 5
    image_count = 0
    for infile in glob.glob(os.path.join(path, '*.jpg')):
        image_count += 1
        r, c = divmod(image_count-1, COLUMNS)
        im = Image.open(infile)
        resized = im.resize((256, 256), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        myvar = tk.Label(win, image=tkimage)
        myvar.image = tkimage
        myvar.grid(row=r, column=c)
    win.mainloop()  # not sure if you need this, too, or not...

messageWindow()