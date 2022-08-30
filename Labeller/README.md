# Ball labeller using Re3 Tracker

This is an implementation of [Re3: Real-Time Recurrent Regression Networks for Visual Tracking of Generic Objects](https://danielgordon10.github.io/pdfs/re3.pdf) expanding on an [implementation by the project supvervisor](https://github.com/r0nn13/ball-labeller) Dr Ronald Clark.

## Labelling new images using the tracker
The images to be labelled should be place in [demo/data/imgs](demo/data/imgs) and should be in .png / jpg format.

Run `python3 demo/app.py`

<img src="/demo/labeller.png" height="300"/>

### Annotation
* **left click** - mark ball at clicked location
* **middle click** - remove annotation from current frame

### Navigation
* **d** - go to next frame 
* **a** - go to previous frame
* **esc** - exit labeller

### Event selection
* **1** select Nothing event
* **2** select Ball event
* **3** select Bounce event
* **4** select Racket Contact event
* **5** select Net Contact event
* **6** select Serve event

After labelling all images or exiting the labeller, a `annotations.txt` file will be created storing the bounding box for each frame.
