from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import os

app = Flask(name)
model = YOLO("yolov9.pt")  # Replace with actual yolov9 path

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    file = request.files["image"]
    img_path = os.path.join("static", "uploaded.jpg")
    file.save(img_path)

    results = model(img_path)
    annotated_frame = results[0].plot()
    output_path = os.path.join("static", "output.jpg")
    cv2.imwrite(output_path, annotated_frame)

    return jsonify({"output_url": output_path})

if name == "_main_":
    app.run(debug=True)