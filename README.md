# 3D_Tennis_Tracker

## TTNet

### Download dataset 

Download dataset from https://drive.google.com/drive/folders/19hsBQrfqSwfX7smjiZeFqzA3R9dyY2ri?usp=sharing. Extract videos.zip into TTNet/Dataset/videos and extract images.zip into TTNet/Dataset/images.

Use ffmpeg to extract frames from each clip. In the videos directory run
```
for i in {01..30}; do ffmpeg -i $i.mp4 -start_number 0 ../images/$i/%04d.jpg; done
```

## Download pretrained models

Download model from https://drive.google.com/drive/folders/1zI0GRQwE52nA8DtBV3Vq_qEJHpHLrEOo?usp=sharing and save to TTNet/Trained_Models/Final
