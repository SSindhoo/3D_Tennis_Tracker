# 3D_Tennis_Tracker

## Download weights

All weights are available at https://drive.google.com/drive/folders/1zI0GRQwE52nA8DtBV3Vq_qEJHpHLrEOo?usp=sharing. 

### Labeller

Save *iteration_0003500.pt* to Labeller/logs/checkpoints/

### TrackNet

Save *TrackNet_Final.pth* to TrackNet/Trained_Models/

### TTNet

Save *TTNet_Final_pth to TTNet/Trained_Models/Final/

## Download datasets

Datasets for both models are available at https://drive.google.com/drive/folders/19hsBQrfqSwfX7smjiZeFqzA3R9dyY2ri?usp=sharing

### TrackNet

Download both *TrackNet_dataset.zip* and *videos.zip* and unzip both into TrackNet/. Use ffmpeg to extract the frames from each video clip. In the directory TrackNet/videos/ run the following command:
```
for i in {01..30}; do mkdir $i && ffmpeg -i $i.mp4 -start_number 0 -vf "scale=1280:720" $i/%06d.jpg; done
```

Then move the images to TrackNet/Dataset/ following the layout given in TrackNet/Dataset/layout.txt 

### TTNet

Download both *TTNet_dataset.zip* and *videos.zip* and unzip both into TTNet/Dataset/. Use ffmpeg to extract the frames from each video clip. In the directory TTNet/Dataset/videos/ run the following command:

```
for i in {01..30}; do mkdir $i && ffmpeg -i $i.mp4 -start_number 0 $i/%04d.jpg; done
```
Then move the images to TTNet/Dataset/images/ following the layout given in TTNet/Dataset/images/layout.txt 
