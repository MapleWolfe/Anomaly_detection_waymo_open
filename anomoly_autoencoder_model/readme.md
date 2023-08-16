This folder focuses on development of a Autoencoder model. specifically we are going to be using an autoencoder, the architecture for which was built using dense layers to allow for a fully connected model. we utilized the dense layers with the relu activation to allow the model to capture non linear representation of data for better understanding of complex data. the autoencoder is an unsupervised model as such there are no labels. the ground truth values are the image themselves. 

the objective of this model is to perform anomaly detection through image reconstruction, by analyzing the mean squared error in reconstruction against a distribution developed on the validation dataset, we were able to identify portions of the image that had possible anomalies.

Instructions to operate Notebook:

To run a sample of the notebok please use google colab (this is the development enviornment of the notebook)
upload the following files / folders into colab: detect_model_requirements.txt and Google Cloud Storage json api key or upload the waymo_sample_data folder from this repository

Kindly fill The first code cell with requested details, it allows you to input your file paths if needed as well as it allows you to decide between using locally uploaded files and GCS. it also takes in the GCS json key file path .
the first cell also allows you to decide the number of files to download and work with from GCS for train and validation respectively.
please review the installs and imports section of the notebook to uncomment and install the libraries or to uncomment and install using detect_model_requirements.txt
** Kindly ensure ** to maintain the original file structure if using data from waymo_sample_data for things to run smoothly. or maintain the file structure from the original waymo data.
