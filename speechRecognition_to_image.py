#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import glob
import speech_recognition as sr
from gtts import gTTS
import os
from pygame import mixer


# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

speech = r.recognize_google(audio)

# The text that you want to convert to audio
mytext = speech

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("speaker.mp3")

# Playing the converted file
mixer.init()
mixer.music.load('speaker.mp3')
# print("You said....")
mixer.music.play()

speech = speech.upper()
speech = speech.replace(" ","")
arr = list(speech)
print(arr)


import shutil

if(os.path.isdir("/Users/rishabpal/PycharmProjects/untitled/saved_images")):
    # To remove an existing directory
    shutil.rmtree("/Users/rishabpal/PycharmProjects/untitled/saved_images")
    # To create a new directory
    os.mkdir("saved_images")
else:
    os.mkdir("saved_images")

import tkinter as tk
from PIL import Image, ImageTk
import numpy

root = tk.Tk()


# position coordinates of root 'upper left corner'
x = 0
y = 0

imageslist = list()
columns = 5
size = 256, 256
var = len(arr)-1
for i in range(0, len(arr)):
    path = '/Users/rishabpal/Documents/speech_database/' + arr[i] + ".jpg"
    # pick an image file you have .bmp  .jpg  .gif.  .png
    # load the file and covert it to a Tkinter image object
    # im = ImageTk.PhotoImage(Image.open(path))
    im = Image.open(path)
    im.thumbnail(size, Image.ANTIALIAS)
    im = ImageTk.PhotoImage(im)


    # Converting the image into numpy array_____________________
    img = Image.open(path)

    img1 = numpy.array(img)

    # fft_mag = numpy.abs(numpy.fft.fftshift(numpy.fft.fft2(img1)))
    #
    # visual = numpy.log(fft_mag)
    # visual = (visual - visual.min()) / (visual.max() - visual.min())
    #
    # result = Image.fromarray((visual * 255).astype(numpy.uint8))
    # result.save('/Users/rishabpal/PycharmProjects/untitled/saved_images/'+str(i)+".jpg")

    img1 = Image.fromarray(img1)
    img1.save('/Users/rishabpal/PycharmProjects/untitled/saved_images/'+str(var)+".jpg")
    var -= 1
    # _________________________________________________________________________________________________________

    # save the panel's image from 'garbage collection'

    # original = Image.fromarray(resized)
    # original = ImageTk.PhotoImage(original)
    imageslist.append(im)

panelA = None
r = 0
c = 0
# panelA.grid(row=r, column=c)
# panelA =
# r, c = divmod(len(speech)-1, columns)
length = len(arr)
if panelA is None:
    # the first panel will store our original image
    for image in imageslist:
        panelA = tk.Label(root, image=image)
        # length -= 1
        # panelA.grid(row=r, column=c)
        c +=1
        if(c>=5):
            r +=1
            c = 0
        panelA.image = image
        panelA.pack(side = "left", fill = "both", expand = "yes")

        # side = "top", fill = "both", expand = "yes"
    # otherwise, update the image panels
else:
    panelA.destroy()
    for image in imageslist:
        panelA = tk.Label(root, image=image)
        # panelA.grid(row=r, column=c)
        c += 1
        if (c >= 5):
            r += 1
            c = 0
        # length -= 1
        panelA.image = image
        panelA.pack(side = "left", fill = "both", expand = "yes")

root.title('Sign Language')
root.resizable(width=False, height=False)
root.mainloop()

from speechRecognition_to_image import messageWindow
messageWindow()