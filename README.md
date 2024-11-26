# Sleep Quality Prediction Project

## Description

This project aims to predict a person's heart rate based on their sleep health and lifestyle factors. In today's fast-paced world, people are often sleep-deprived and have unhealthy lifestyles. Poor quality of sleep can affect an individual's overall health condition including heartrate, which is a good indicator of the overall health. This project seeks to use a machine learning model to predict a person's heart rate in order to predict their overall well-being, and to determine if they may be at higher risk of developing a sleep disorder.

Goal The goal of this project is to build a predictive model using the provided lifestyle and sleep health dataset. The trained model will give the approximate heartrate of a person which is a key metric for checking overall health. The model can help identify individuals who may be at higher risk of health issues, allowing for preventative measures and improved healthcare outcomes.

How the model can help Predictive insights: The model can provide insights into an individual's potential risk of heart rate problems and, by extension their overall health and sleep health problems. Early detection: By predicting heart rate based on lifestyle and health data, the model enables early detection of potential issues and facilitates timely intervention strategies. Personalized recommendations: The model's predictions allow for personalized recommendations tailored to individual risk profiles. By using it, individuals can know their risk levels and take proactive steps to manage their sleep habits and lifestyle.

## Instructions on How to Run the Project

1. **Install Dependencies:**
2. **Download the dataset:**
   - Download the "Sleep_health_and_lifestyle_dataset.csv" file from ["import kagglehub path = kagglehub.dataset_download("uom190346a/sleep-health-and-lifestyle-dataset"].
   - Place it in the project's root directory.

3. **Run the notebook:**
   - Open the `notebook.ipynb` file in Google Colab or Jupyter Notebook.
   - Execute all cells to train the model and evaluate its performance.

4. **Run the prediction service (optional):**
   - Run the `predict.py` script to start a web service for making predictions.
   - Send requests to the service with input data to receive predictions.

**Note:** You may need to adjust file paths or settings based on your environment.
