# Yolo Model Creation
This folder focuses on development of a YOLO (You only look once) model. specifically we are going to be using YOLOv8. the architecture for YOLOV8 focuses on targets observed in the WAYMO open data set, more specifically it targets the five annoted label objects:

- 0: undefined
- 1: vehicle
- 2: pedestrian
- 3: sign
- 4: cyclist

Yolo effectively identifies and locates objects within the image and creates bounding boxes on them (the model doesn't directly plot it gives their coordinates). it also provides class labels of the detected object, in our case one of the above 5. the **yolov8_waymo.yaml** is that we built contains the list of classes. 

Instructions to operate Notebook:
  1. to run a sample of the notebok please use google colab (this is the development enviornment of the notebook)
  2. upload the following files / folders into colab:
     **yolov8_waymo.yaml** , **detect_model_requirements.txt** and **Google Cloud Storage json api key** or upload the                       **waymo_sample_data folder** from this repository
  3. Kindly fill The first code cell with requested details, it allows you to input your file paths if needed as well as it allows you       to decide between using locally uploaded files and GCS.  it also takes in the GCS json key file path .
  4. the first cell also  allows you to decide the number of files to download and work with from GCS for train and validation               respectively.
  5. please review the installs and imports section of the notebook to uncomment and install the libraries or to uncomment and install       using detect_model_requirements.txt

** Kindly ensure ** to maintain the original file structure if using data from waymo_sample_data for things to run smoothly. or maintain the file structure from the original waymo data.

The yolo v8 model architecture was a part of the Ultralytics library. the library is released on AGPL 3.0. as requested by the author please review the below citation for the model architecture that was used in this folder:

<img width="1230" alt="yolo_v8_attribution" src=yolo_attribution.png>
