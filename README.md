# Anomaly_detection_waymo_open
Capstone Project - Team Rouges of the Unviersity of Michigan Master's of Applied Data Science (MADS) program. 
(Insert Names Here)

## Introduction
We aim to develop a model specifically tailored for autonomous driving scenarios for helping an anomaly-object detection system of autonomous driving using the Waymo Open Source Dataset. Our project aims to leverage machine learning techniques to identify and label anomalous objects in perception 2D camera data in order to further enhance the safety and reliability of autonomous vehicles (AV). One such application of our resulting model could be the implementation of a more robust motion-prediction-behavior model based on the types of classifications we acquire. For example, whether the object classified is mobile or immobile and how to react to such an occurrence. More and more people are interested in using autonomous driving functionalities to help their driving; whether for personal use or for business, therefore, it is essential and important to improve the safety, reliability, and performance of AV.

## Related Work
Inspired by a related work done by scientific researchers in the Karlsruhe Institute of Technology in Germany, Bogdoll et al. consider a multimodal approach towards unknown objects for AV. The application of semantic segmentation, clustering, and 3D object detection (on the lidar data) is an inspiration towards our pipeline in approaching our image-based data. Multimodal approaches may benefit our current work, but at this current time, it is yet to be seen whether it’ll be truly beneficial towards our current goal.

## Model Development
In the related work we found, the researchers converted the 3D data to 2D data and they had a pretrained model for classification work. We would like to **emphasize** that we will directly use 2D data and in their work they only classified the vehicles, pedestrians, signs and cyclists as normal objects and all the other ones are classified as anomalies. For this section, we will put more effort into making improvements to make the anomaly detection to be more accurate and be capable of covering more uncommon anomalies by utilizing pretrained models like Yolo.

Our anomaly detection segmentation pipeline is the following: Yolo V7 that creates a 2D bounding box and classifies the image, followed by UNet to perform pixel segmentation on the portion of the image within the bounding box (This should help with processing speed since segmentation is computationally intensive), and lastly we will layer the mask output and label names on the original image to create an output for the classification of all objects in the user provided image. We will be using a variety of methods at this point to identify anomalies, including if the label had  frequent / infrequent occurrence in the original dataset, using Yolo model label certainty percentage and possible clustering to identify if images fall within commonly  occurring labels. Since the Waymo model ideally should be able to label even anomalous objects on the road, we can have our dashboard allow the user to edit the output tags ( our goal is for the dashboard output a new parquet file in the same format as the  original waymo data with the new labels (including anomalies) and segmentation).

Implementation of a UNet CNN-based architecture towards 2D images gathered from AV camera data. The UNet model, originally used towards biomedical sciences, is a strong resource for semantic segmentation in terms of data input size and GPU usage. Meaning, we can use few images and still retain strong validation metrics resulting in a lower computational cost. To tune this model, we will vary certain hyperparameters such as loss and numbers of layers; then compare by validation curves. Layers will also be judged by activation maps. Otherwise, the base architecture will follow the UNet architecture as provided by Ronneberger et al. 

-------------------------------------------------------------------------------------------------------------------

### Important Links

| Title | Description | Link |
|-------|-------------|--------|
| Waymo | Location of Data | https://waymo.com/ | 
| YOLOv7 | Paper citation and information of pretrained model for bounding boxes | https://arxiv.org/abs/2207.02696 |
| U-Net | Paper citation and information of U-Net archetecture | https://arxiv.org/abs/1505.04597 |
