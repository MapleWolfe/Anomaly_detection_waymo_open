# Yolo Model Creation
This folder focuses on development of a YOLO (You only look once) model. specifically we are going to be using YOLOv8. the architecture for YOLOV8 focuses on targets observed in the WAYMO open data set, more specifically it targets the five annoted label objects:

1: vehicle
2: pedestrian
3: sign
4: cyclist

Yolo effectively identifies and locates objects within the image and creates bounding boxes on them (the model doesn't directly plot it gives their coordinates). it also provides class labels of the detected object, in our case one of the above 4 or 'undefined' if it can't identify the model. the **yolov8_waymo.yaml** is that we built contains the list of classes. 

Instructions to operate Notebook:
  1. to run a sample of the notebok please use google colab (this is the development enviornment of the notebook)
  2. upload the following files / folders into colab:
     **yolov8_waymo.yaml** , **detect_model_requirements.txt** and **Google Cloud Storage json api key** or upload the                       **waymo_sample_data folder** from this repository
  3. Kindly fill The first code cell with requested details, it allows you to input your file paths if needed as well as it allows you       to decide between using locally uploaded files and GCS.  it also takes in the GCS json key file path .
  4. the first cell also  allows you to decide the number of files to download and work with from GCS for train and validation               respectively.
  5. please review the installs and imports section of the notebook to uncomment and install the libraries or to uncomment and install       using detect_model_requirements.txt

Notebook H

*** Kindly ensure** to maintain the original file structure if using data from waymo_sample_data for things to run smoothly. or maintain the file structure from the original waymo data.

The yolo v8 model architecture was a part of the Ultralytics library. the library is released on AGPL 3.0. as requested by the author please review the below citation for the model architecture that was used in this folder:

@software{yolov8_ultralytics,
  author = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},
  title = {Ultralytics YOLOv8},
  version = {8.0.0},
  year = {2023},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}

