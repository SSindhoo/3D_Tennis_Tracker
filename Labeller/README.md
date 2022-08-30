# Ball labeller using Re3 Tracker

This repository is based on the official implementation of [Re3: Real-Time Recurrent Regression Networks for Visual Tracking of Generic Objects](https://danielgordon10.github.io/pdfs/re3.pdf).

## Training the tracker on tennis images
The following fils are needed for training the tracker:
1. [training/datasets/tennis/imgs](training/datasets/tennis/imgs) - the RGB images for training (.png)
2. [training/datasets/tennis/labels/train/labels.npy](training/datasets/tennis/labels/train/labels.npy) - the labels for the images 
3. [training/datasets/tennis/labels/train/image_names.txt](training/datasets/tennis/labels/train/image_names.txt) - the names of the images
4. (optional) [logs/checkpoints/iteration_0003500.pt](logs/checkpoints/iteration_0003500.pt) - the pretrained model

To train the model simply run: `python3 training/unrolled_solver.py -rtc -n 2 -b 64`

## Labelling new images using the tracker
The images to be labelled should be place in the following directories:
1. [demo/data/imgs](demo/data/imgs) - the images should be in .png / jpg format

Run `python3 demo/image_demo.py`

<img src="/demo/tennis_demo.png" height="300"/>

**left click** - mark ball at clicked location,
**middle click** - remove ball from frame,
**spacebar** - go to next frame 

After finishing all frames in the video, a `locations.txt` file will be created storing the ball bounding box for each frame.
