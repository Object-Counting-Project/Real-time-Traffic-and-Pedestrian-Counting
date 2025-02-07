# Real-time-Traffic-and-Pedestrian-Counting

<h3>Introduction</h3>
<h4>This project aims to count vehicle and pedestrian detected in the input video using YOLOv5 object-detection algorithm with the KalmanBoxTracker for tracking objects</h4>

<h4>It needs to be stated that YOLOv5 object-detection is forked from the implementation of 
<a href="https://github.com/ultralytics/yolov5?fbclid=IwAR3mJzN0aLJZY0qLzXeuuZo5OwfOYZ_BHLNs5bZo3N4dDEHfLg0HnZZRbDs">glenn-jocher</a>, and "KalmanBoxTracker" tracking implementation forked from 
<a href="https://github.com/clemente0420/Real-time-Traffic-and-Pedestrian-Counting?fbclid=IwAR1O0PaEmcSf4E4m6_It6hMCTJD2UJl70S6O-XZd4UL_086ig9upg5NGZ-g">clemente0620</a></h4>

<h4>Using the PyTorch Object detection API(YOLOv5 is written in the Pytorch framework), we will be counting the number of vehicles and pedestrians in a video. A frame is extracted every second from the video and a forward pass of the model is performed. If a vehicle or pedestrian is found in the video, then the count is increased.
</h4>

<h4>In order to achieve the best performance, you should have CUDA installed on Your device.</h4>
<hr>

<h3>Project Demo</h3>
https://user-images.githubusercontent.com/47077167/115262112-e6f72b80-a13c-11eb-8e77-e8697e74df9b.mp4




![175490636_1602961063227825_8176010990751348582_n](https://user-images.githubusercontent.com/47077167/115276791-28db9e00-a14c-11eb-81c5-b49629e999da.png)

<hr>



<h3>Run Demo</h3>

```html
python detect.py --source video.mp4
```

<hr>

<h3>Usage</h3>

```html
python3 app.py
```

<hr>



<h3>Web Hosting</h3>
<h5>
Inorder to host the model we used FloyHub which offers 2 hours of free

usage form their standard instance with the following specs:

GPU: Tesla K80 · VRAM :12 GB Memory · RAM: 61 GB RAM · Storage: 100 GB SSD</h5>

<hr>

<h3>Database</h3>
<h5>The count of vehicles and people periodically gets pushed to a cloud MongoDb cluster every minute, and there’s charts in the dashboard that summarize this data and are updated in real-time</h5>

<hr>

<h3>Author</h3>

<a href="https://github.com/ultralytics/yolov5?fbclid=IwAR3mJzN0aLJZY0qLzXeuuZo5OwfOYZ_BHLNs5bZo3N4dDEHfLg0HnZZRbDs">glenn-jocher</a> yolov5<br>
<a href="https://github.com/clemente0420/Real-time-Traffic-and-Pedestrian-Counting?fbclid=IwAR1O0PaEmcSf4E4m6_It6hMCTJD2UJl70S6O-XZd4UL_086ig9upg5NGZ-g">clemente0620 </a></h4>Real-time-Traffic-and-Pedestrian-Counting
