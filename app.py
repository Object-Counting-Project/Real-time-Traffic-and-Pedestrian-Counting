from flask import Flask, render_template, Response, request, send_file, jsonify, make_response
import requests
import cv2
import numpy as np
from detect import detect
from models.experimental import attempt_load
from utils.torch_utils import select_device
from utils.general import set_logging
from pymongo import MongoClient

app = Flask(__name__, static_folder='static')


youtube_link = 0


def edit_link(new_link):
    global youtube_link
    youtube_link = new_link


@app.route('/')
def index():
    # Video streaming home page.
    return render_template('index.html')


@app.route('/render_feed', methods=["GET", "POST"])
def render_feed():

    edit_link(request.form['youtube_link'])

    # Video streaming home page.
    return render_template('video_feed.html')


@app.route('/video_feed')
def video_feed():

    # Video streaming route. Put this in the src attribute of an img tag.
    return Response(detect(youtube_link, model, device, database),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':

    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    client = MongoClient(
        "mongodb+srv://user:1234@cluster0.vfc9s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    database = client.counts

    weights = './yolov5s.pt'

    device = select_device("")

    model = attempt_load(weights, map_location=device)  # load FP32 model

    app.run(host='0.0.0.0', threaded=False, debug=True)
