# U-Net Model Creation
This folder focuses on preprocessing and implementation of a U-Net model architecture focusing on targets seen in the WAYMO open data set, more correctly their Preception data. 
The goal is to segment 2D camera images and then relayer the segmentation results onto the original RGB image.

Python scripts are utilized in the notebooks as helper functions for enabling a less bulky read.

## Helper Scripts
For building the architecture of the model:
- build_unet.py
- unet_build_blocks.py

For preprocessing the data and some other helper functions
- helper.py
- transforms.py

## The Visualization 
Resulted from the unet_v2 notebook is an altair based visualization on Loss results from hyperparameter tuning. Results should be similar to:
[[]]
