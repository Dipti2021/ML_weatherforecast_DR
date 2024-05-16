import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

def load_data():
    return pd.read_csv('weather_forecast.csv')

# Load logistic regression model
logistic_model = joblib.load('logistic_regression_weather_model.pkl')

# Load random forest model
random_forest_model = joblib.load('random_forest_weather_model.pkl')

def show_predict_page():
    st.title("Weather Prediction")
    st.write("This page allows you to make predictions based on weather data.")

    # Load data
    df = load_data()

    # Get input features
    label_encoder = LabelEncoder()
    label_encoder.fit(df['City'])
    city = st.selectbox("Select a city", df['City'].unique())
    processed_city = label_encoder.transform([city])[0]

    date = st.date_input("Select a date")
    processed_date = pd.to_datetime(date).toordinal()

    # Display prediction for logistic regression model
    if st.button("Predict with Logistic Regression"):
        # Make prediction using the logistic regression model
        logistic_prediction = logistic_model.predict([[processed_city, processed_date]])
        st.write("Predicted weather description (Logistic Regression):", logistic_prediction)

    # Display prediction for random forest model
    if st.button("Predict with Random Forest"):
        # Make prediction using the random forest model
        random_forest_prediction = random_forest_model.predict([[processed_city, processed_date]])
        st.write("Predicted weather description (Random Forest):", random_forest_prediction)

if __name__ == "__main__":
    show_predict_page()
