# AiBxDarun Image Classification : Real human face or AI-generated
A classification model for predicting if the image is a real human face or AI-generated human face.

# Feature of This Model
This model can predict between real and fake (AI-generated) human face images with performance more than 99% accuracy.

# Dataset used to train this model
The dataset are from 'ArtiFact: Real and Fake Image Dataset'.
- Kaggle : https://www.kaggle.com/datasets/awsaf49/artifact-dataset
- Github : https://github.com/awsaf49/artifact?tab=readme-ov-file

The folder in this Dataset that had been used are:
For the real images (30k images in total)
1. CelebAHQ

For the fake images (29,995 images in total)
1. StarGAN
2. SFHQ
3. FaceSynthetics

Then separate them into training dataset with 60% of total images, validation dataset with 20% of total images, and testing dataset with 20% of total images.

# About the Model
- Resnet34 model
- FastAI libary for training this model.
- Accuracy metrics for checking the performance of the model with 3 epoch of training.

# Links
- For further details about this model (written in Thai) : https://medium.com/@bunpan.kaopun/image-classification-real-human-face-or-ai-generated-image-cf8db20b2b58
- For using the model (on streamlit) : https://aibxdarun-image-classification-real-human-face-or-ai-generated.streamlit.app/
