
Here we illustrate the alternatives between the model when using different versions of YOLO object detection and framework

TRIAL 1 : MobileNet v1

We worked on MobileNet v1 which has been trained on the COCO dataset  and use DeepSORT to Track the  Objects.

MobileNet based on a streamlined architecture that uses depthwise separable convolutions to build lightweight 
deep neural networks that can have low latency for mobile and embedded devices.

The network consists of 28 convolutional layers and 1 fully connected layer followed by a softmax layer. 
Batch normalization and ReLU is applied after convolution

** It uses TensorFlow Lite as framework **

** We ran MobileNet v1 in a CPU environment, and it was capable of processing 1.5 frames per second. **

Because the number of frame per second is very small, we will use another architecture 
---------------------------------------------

TRIAL 2 : YOLOv3

We work on YOLOv3 which was Implemented in Tensorflow2.It uses Darknet 53 architecture, 
which was a significantly improved version and had 53 convolution layers and it uses KalmanBoxTracker to Track the  Objects

** It uses TensorFlow as framework **

** We ran YOLOv3 in a CPU(i7 10750H) environment, and it was capable of processing 3.5 frames per second. **

Still the number of frames per second small, we need MORE frames !!!

We have three options for increasing the # of frames :
1- Reduce resolution
2- Use "yolo-tiny" object detection
3- Use GPU 

---------------------------------------------

TRIAL 3 : YOLOv3-tiny

We chose option 2 in order to increase the number of frames

** It uses TensorFlow as framework **

** We ran YOLOv3-tiny in a CPU(i7 10750H) environment, and it was capable of processing 2 frames per second. **

This option does not work as we thought!!!

---------------------------------------------

TRIAL 4 : YOLOv3/GPU

Here we tried to run the YOLOv3 on GPU environment using CUDA (gives direct access to GPU).
Becuse we tried to put too much data on CUDA. As a result it failed

** CUDA_ERROR_OUT_OF_MEMORY: out of memory **


---------------------------------------------

TRIAL 5 : YOLOv5

Because the previous trial keeps giving "out of memory", we will use YOLOv5 since it is much more lightweight and easy to use

YOLOv5 is the first of the YOLO models to be written in the PyTorch framework. It uses CSPDarknet53 architecture

** We ran YOLOv5 in a CPU(i7 10750H) environment, and it was capable of processing 8 frames per second. **

** We ran YOLOv5 in a GPU environment, and it was capable of processing 100 frames per second.!!!! **
 
NOTE : All the above trials uses tensorflow framework BUT yolov5 use pytorch framework







