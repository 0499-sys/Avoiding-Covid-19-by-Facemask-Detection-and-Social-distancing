# Avoiding-Covid-19-by-Facemask-Detection-and-Social-distancing

## Overview

The **Facemask-Detection-and-Social-distancing** is an automated solution designed to enhance public safety by monitoring face mask usage and enforcing social distancing protocols in real-time. By leveraging computer vision and deep learning techniques, this system aims to mitigate the spread of infectious diseases, particularly during health crises like the COVID-19 pandemic.

## Features

### 1. Face Mask Detection
- **Real-Time Monitoring**: Utilizes webcam and video input to detect whether individuals are wearing face masks.
- **Automated Alerts**: Sends notifications via email to users when a mask is not detected.

### 2. Social Distancing Detection
- **Distance Calculation**: Employs Euclidean distance metrics to ensure individuals maintain a safe distance from each other.
- **Visual Feedback**: Violating individuals are highlighted in red, while those in compliance are displayed in green.

### 3. User Authentication
- **Secure Access**: Provides login and signup functionality for users to track compliance in designated areas.

## Technologies Used

- **Programming Languages**: Python
- **Computer Vision Libraries**: 
  - OpenCV: For image and video processing.
  - TensorFlow/Keras: For building and training machine learning models.
- **Machine Learning Techniques**:
  - Haar Cascade Classifier: For initial face detection.
  - Convolutional Neural Networks (CNN): For face mask detection.
- **Distance Calculation**: Euclidean distance formula to assess spatial relationships between detected individuals.
- **Email Automation**: SMTP libraries for sending alerts when violations are detected.

## Key Functionalities
- **Accurate Face Mask Detection**: Effectively identifies improper mask usage, including masks worn incorrectly or attempts to cover the face with hands.
- **Social Distancing Monitoring**: Visually represents adherence to social distancing guidelines, facilitating immediate intervention when necessary.

## Applications

### 1. Airports
- Monitors travelers for mask compliance and social distancing, allowing for immediate action by airport authorities.

### 2. Hospitals
- Ensures healthcare workers and quarantined individuals follow safety protocols, with alerts sent to authorities for any violations.

### 3. Offices
- Tracks employee compliance with health standards, generating end-of-day reports for management review.

### 4. Public Spaces
- Applicable in various settings, including shopping malls, metro stations, temples, and other crowded areas to enhance overall public safety.

## Results

![image](https://github.com/user-attachments/assets/6933b57c-ff5f-489a-8944-1ff46a12b9e7)

![image](https://github.com/user-attachments/assets/da18e646-5c25-4aa5-9cda-38c62e0a0a6e)

![image](https://github.com/user-attachments/assets/afdbc09a-29e5-49a7-bd0e-aac4318eefac)

![image](https://github.com/user-attachments/assets/caba6fd9-6f1e-426f-848b-9d48f72fac35)

![image](https://github.com/user-attachments/assets/63da0d95-340f-437f-989c-9f5e227ed8fb)

![image](https://github.com/user-attachments/assets/67dd5dd4-5ab8-428a-acec-cb4312fe391a)

![image](https://github.com/user-attachments/assets/296056a7-f4dc-4784-a924-f4ba89e8b7d1)

## Constraints

- **Lighting Sensitivity**: The HaarCascadeClassifier can produce false detections under varying lighting conditions and may struggle with side profiles.
- **Threshold Distance Limitations**: Fixed threshold distances for social distancing can vary based on camera placement, potentially affecting accuracy.

## Strengths

- **Comprehensive Mask Detection**: Recognizes not only the presence of masks but also improper usage, such as wearing masks below the nose.
- **Adaptive Alerting Mechanism**: Detects attempts to disguise non-compliance, including covering the face with hands.

## Future Scope

- **Coughing and Sneezing Detection**: Utilize deep learning to monitor respiratory symptoms, enhancing public health response.
- **Thermal Screening Integration**: Equip the system with thermal cameras for non-contact temperature screening, further bolstering public health safety measures.

## Conclusion

The Social Distancing and Face Mask Detection System effectively monitors compliance with essential health guidelines, contributing to public safety and reducing disease transmission. Successfully tested in real-time scenarios, this project has significant potential to enhance health security measures across various public environments.
