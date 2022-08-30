import os
import sys
import glob

import numpy as np
from tkinter import *
from PIL import ImageTk, Image, ImageDraw 

# Configuring Directories
basedir = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.join(basedir, os.path.pardir)))
image_paths = sorted(glob.glob(os.path.join(
    os.path.dirname(__file__), "data", "imgs", "*.png")))
from tracker import re3_tracker

# Initialise tracker
tracking = False
tracker = re3_tracker.Re3Tracker()
first_track = True

# Setup
annotations = np.zeros((1,5))
frame_no = 0
seen_frames = 0
frame_count = len(image_paths)

# SCALE CONFIGURATION. If HD 1.2, 15. If 720p 1.0, 12
SCALE= 1.2
BBOX_OFFSET = 12

# Window config
root = Tk()
root.title(str(frame_no+1) + " / " + str(frame_count))

# Display the image
def display_image(img_path):
    global img_label

    i = Image.open(img_path)
    draw=ImageDraw.Draw(i)
    anno = annotations[frame_no]

    # Blue if prior frame, red if tracking
    draw.rectangle([(anno[1],anno[2]),(anno[3],anno[4])],outline="blue")
    if tracking:
        draw.rectangle([(anno[1],anno[2]),(anno[3],anno[4])],outline="red")

    i.thumbnail((1600, 900), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(i)
    img_label.config(image=img)
    img_label.photo_ref = img
    root.title(str(frame_no+1) + " / " + str(frame_count))

def annotate(event):
    global selected_event
    global frame_no
    global annotations
    global tracking

    bbox = [(event.x*SCALE)-BBOX_OFFSET, (event.y*SCALE)-BBOX_OFFSET, (event.x*SCALE)+BBOX_OFFSET, (event.y*SCALE)+BBOX_OFFSET]
    annotations[frame_no, 0] = selected_event.get()
    annotations[frame_no, 1:] = bbox
    if (frame_no == seen_frames): 
            tracking = True
            tracker.track("ball", image_paths[0], bbox)
            print("Annotated")

def clear(event):
    global tracking

    tracking = False
    annotations[frame_no, 0] = 0
    annotations[frame_no, 1:] = 0.0

i = Image.open(image_paths[frame_no])
i.thumbnail((1600, 900), Image.ANTIALIAS)
img = ImageTk.PhotoImage(i)
img_label = Label(image=img)
img_label.bind('<Button-1>', annotate)
img_label.bind('<Button-2>', clear)
img_label.grid(row=0, column=0, rowspan=200)

# Event Selection
label = Label(text="Select Annotation Label:")
label.grid(padx=5, pady=5, row=0, column=1, columnspan=2)

selected_event = IntVar()
r1 = Radiobutton(root, text="Nothing", value=0, variable=selected_event)
r2 = Radiobutton(root, text="Ball", value=1, variable=selected_event)
r3 = Radiobutton(root, text="Bounce", value=2, variable=selected_event)
r4 = Radiobutton(root, text="Racket Contact", value=3, variable=selected_event)
r5 = Radiobutton(root, text="Net Contact", value=4, variable=selected_event)
r6 = Radiobutton(root, text="Serve", value=5, variable=selected_event)
rbtns = [r1, r2, r3, r4, r5, r6]
for i, rbtn in enumerate(rbtns):
    rbtn.grid(row=i+1, column=1, columnspan=2, sticky="W")

root.bind('<KeyPress-1>', lambda event: selected_event.set(0))
root.bind('<KeyPress-2>', lambda event: selected_event.set(1))
root.bind('<KeyPress-3>', lambda event: selected_event.set(2))
root.bind('<KeyPress-4>', lambda event: selected_event.set(3))
root.bind('<KeyPress-5>', lambda event: selected_event.set(4))
root.bind('<KeyPress-6>', lambda event: selected_event.set(5))

def track():
    global selected_event

    bbox = tracker.track("ball", image_paths[frame_no])
    annotations[frame_no+1, 0] = selected_event.get()
    annotations[frame_no+1, 1:] = bbox

# Button Commands
def next():
    global frame_no
    global seen_frames
    global annotations
    global tracking
    global first_track

    if seen_frames == frame_no:
        seen_frames += 1
        annotations = np.vstack([annotations, np.zeros((1,5))]) # Make space in annotations
        
        # Track if there is a bbox in current frame
        if not np.array_equal(annotations[frame_no, 1:], np.zeros((4))):
            tracking = True
        if tracking:
            if first_track:
                track()
                first_track = False
            track()
        np.savetxt('annotations.txt', annotations[:], '%.1d')
    frame_no = min(frame_no+1, frame_count-1)
    display_image(image_paths[frame_no])

def prev():
    global frame_no
    global seen_frames
    global tracking

    tracking = False
    frame_no = max(0, frame_no-1)
    display_image(image_paths[frame_no])

def exit():
    np.savetxt('annotations.txt', annotations[:], '%.1d')
    root.quit()

b1 = Button(root, text='Previous Image', command=prev)
b1.grid(row=7, column=1, sticky='W')
b2 = Button(root, text='Next Image', command=next)
b2.grid(row=7, column=2, sticky='W')
b3 = Button(root, text='Save & Exit', command=exit)
b3.grid(row=8, column=1, columnspan=2)

root.bind('<KeyPress-a>', lambda event: prev())
root.bind('<KeyPress-d>', lambda event: next())
root.bind('<Escape>', lambda event: exit())

root.mainloop()