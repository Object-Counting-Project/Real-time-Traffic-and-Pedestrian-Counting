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

<hr>

<h3>Flow</h3>

<hr>

<h3>Installation</h3>

<div style="color:blue;text-align:center"> 
<h5>pip install -r requirements.txt</h5>

<h5 style="color:green;">python detect.py --weights yolov5s.pt</h5>

<h5>python detect.py --source video.mp4</h5>

</div>


```html
<!doctype html>
<html>
	<head>
		<title>
			My Website
		</title>
	</head>
	<body>
		Hello, World!	
	</body>
</html>
```

So, what are we looking at here?
HTML, short for *HyperText Markup Language*, consists of these things called tags, which are words written between `<` and `>` characters, like `<sometag>`.  All tags (with just a few exceptions that we'll talk about later) have a matching closing tag, which has the same name as the opening tag, except that it contains `/` after the first `<`, like `</sometag>`. 

For example, `<html>` is one tag and the closing tag for it is `</html>`, same with `<head>` and `</head>` and `<body>` and `</body>`, and so on.  You get it.
The opening and closing tags together are an *element* (which also includes everything written in it).  For example, `<title>My Website</title>` is one element.  The text inside an element, in the title case, `My Website`, is called the *content* of an element.




<hr>

<h3>Run Demo</h3>
<h5>python3 app.py</h5>
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
