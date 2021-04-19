import time
import cv2
import torch
import torch.backends.cudnn as cudnn
from utils.datasets import LoadStreams
from utils.general import check_img_size, non_max_suppression, \
    scale_coords
from utils.torch_utils import time_synchronized
import core.utils as utils
import tensorflow as tf
import numpy as np

from pprintpp import pprint
import copy


def detect(source, model, device, database):

    counter_dict = {}
    prev_dict = {}

    imgsz = 640

    webcam = True

    # Initialize

    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(imgsz, s=stride)  # check img_size
    if half:
        model.half()  # to FP16

    cudnn.benchmark = True  # set True to speed up constant image size inference
    dataset = LoadStreams(source, img_size=imgsz, stride=stride)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[np.random.randint(0, 255) for _ in range(3)] for _ in names]

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(
            next(model.parameters())))  # run once
    startPushTime = time.time()
    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        prev_time = time.time()

        # Inference
        t1 = time_synchronized()
        pred = model(img, augment=True)[0]
        # Apply NMS
        pred = non_max_suppression(
            pred, 0.25, 0.45, agnostic=True)
        t2 = time_synchronized()

        # Process detections
        for i, det in enumerate(pred):  # detections per image

            if webcam:  # batch_size >= 1
                p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(
                ), dataset.count
            else:
                p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)

            # normalization gain whwh
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(
                    img.shape[2:], det[:, :4], im0.shape).round()

                frame = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
                det = det.tolist()

                curr_time = time.time()
                exec_time_1 = curr_time - prev_time
                fps = 1/exec_time_1

                image, counter_dict = utils.video_draw_bbox(frame, det, fps)

                if time.time() - startPushTime > 60:
                    dictToPush = {"pushTime": time.time()}
                    startPushTime = time.time()

                    try:
                        dictToPush["person"] = {"up": counter_dict["person"]["up"] - prev_dict["person"]["up"], "down": counter_dict["person"]["down"] - prev_dict["person"]
                                                ["down"], "left": counter_dict["person"]["left"] - prev_dict["person"]["left"], "right": counter_dict["person"]["right"] - prev_dict["person"]["right"]}
                    except:
                        if "person" in counter_dict.keys():
                            dictToPush["person"] = counter_dict["person"]
                    try:
                        dictToPush["car"] = {"up": counter_dict["car"]["up"] - prev_dict["car"]["up"], "down": counter_dict["car"]["down"] - prev_dict["car"]
                                             ["down"], "left": counter_dict["car"]["left"] - prev_dict["car"]["left"], "right": counter_dict["car"]["right"] - prev_dict["car"]["right"]}
                    except:
                        if "car" in counter_dict.keys():
                            dictToPush["car"] = counter_dict["car"]
                    try:
                        dictToPush["motorcycle"] = {"up": counter_dict["motorcycle"]["up"] - prev_dict["motorcycle"]["down"], "down": counter_dict["motorcycle"]["down"] - prev_dict["motorcycle"]
                                                    ["up"], "left": counter_dict["motorcycle"]["left"] - prev_dict["motorcycle"]["left"], "right": counter_dict["motorcycle"]["right"] - prev_dict["motorcycle"]["right"]}
                    except:
                        if "motorcycle" in counter_dict.keys():
                            dictToPush["motorcycle"] = counter_dict["motorcycle"]
                    try:
                        dictToPush["bus"] = {"up": counter_dict["bus"]["up"] - prev_dict["bus"]["up"], "down": counter_dict["bus"]["down"] - prev_dict["bus"]
                                             ["down"], "left": counter_dict["bus"]["left"] - prev_dict["bus"]["left"], "right": counter_dict["bus"]["right"] - prev_dict["bus"]["right"]}
                    except:
                        if "bus" in counter_dict.keys():
                            dictToPush["bus"] = counter_dict["bus"]
                    try:
                        dictToPush["truck"] = {"up": counter_dict["truck"]["up"] - prev_dict["truck"]["up"], "down": counter_dict["truck"]["down"] - prev_dict["truck"]
                                               ["down"], "left": counter_dict["truck"]["left"] - prev_dict["truck"]["left"], "right": counter_dict["truck"]["right"] - prev_dict["truck"]["right"]}
                    except:
                        if "truck" in counter_dict.keys():
                            dictToPush["truck"] = counter_dict["truck"]

                    result = database.counts.insert_one(dictToPush)
                    print(result)
                    prev_dict = copy.deepcopy(counter_dict)

                result = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                frame = cv2.imencode('.jpg', result)[1].tobytes()

                yield (b'--frame\r\n'b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')


if __name__ == '__main__':

    detect("https://www.youtube.com/watch?v=wqctLW0Hb_0&t=537s")
