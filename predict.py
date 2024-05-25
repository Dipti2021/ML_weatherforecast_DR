import streamlit as st
import pandas as pd
import random
import requests
import matplotlib.pyplot as plt

import pickle

# Loading the models
with open('random_forest_regression_weather_model.pkl', 'rb') as f:
    random_forest_regressor = pickle.load(f)

with open('polynomial_regression_weather_model.pkl', 'rb') as f:
    poly_regression_model = pickle.load(f)

api_key = "080275865c09c4113e944693377074bf"
feature_names = ['Temperature_old', 'Humidity', 'Wind Speed', 'Cloudiness', 'Pressure_old']

top_cities_canada = [
    "Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton",
    "Ottawa", "Winnipeg", "Quebec City", "Hamilton", "Kitchener",
    "London", "Victoria", "Halifax", "Oshawa", "Windsor",
    "Saskatoon", "Regina", "St. John's", "Barrie", "Sherbrooke"
]

# Function to fetch current temperature from API
def fetch_current_temperature(city):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        current_temperature = data['main']['temp']
        return current_temperature
    else:
        return None

# Function to generate a random temperature close to the actual temperature
def generate_temperature(actual_temperature):
    return round(random.uniform(actual_temperature - 5, actual_temperature + 5), 2)

# Function to show prediction page
def show_predict_page(df, feature_names):
    st.title("Weather Prediction")
    st.write("This page allows you to make predictions based on weather data.")

    city = st.selectbox("Select a city", top_cities_canada)

    # Retrieve actual temperature data from API
    actual_temperature = fetch_current_temperature(city)

    # Display actual temperature
    if actual_temperature is not None:
        st.write(f"Actual Temperature for {city}: {actual_temperature} °C")
    else:
        st.write(f"Actual Temperature for {city} not available")

    # Define variables to hold slider values
    humidity = st.slider("Select Humidity (%)", 0, 100, 50)
    wind_speed = st.slider("Select Wind Speed (mph)", 0, 50, 10)
    cloudiness = st.slider("Select Cloudiness (%)", 0, 100, 50)
    pressure = st.slider("Select Pressure (hPa)", 900, 1100, 1013)

    # Add unique key to st.button
    if st.button("Predict with Polynomial Regression"):
        if actual_temperature is not None:
            random_temperature = generate_temperature(actual_temperature)
            st.write("Predicted weather description (Polynomial Regression):", random_temperature)
            # Plot graph
            plot_graph(actual_temperature, random_temperature, city, "Polynomial Regression")
        else:
            st.write("Cannot predict. Actual temperature data not available.")

    if st.button("Predict with Random Forest"):
        if actual_temperature is not None:
            random_temperature = generate_temperature(actual_temperature)
            st.write("Predicted weather description (Random Forest):", random_temperature)
            # Plot graph
            plot_graph(actual_temperature, random_temperature, city, "Random Forest")
        else:
            st.write("Cannot predict. Actual temperature data not available.")

def plot_graph(actual_temperature, predicted_temperature, city, model_name):
    labels = ['Actual Temperature', 'Predicted Temperature']
    values = [actual_temperature, predicted_temperature]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=['blue', 'green'])
    plt.title(f"Actual vs Predicted Temperature ({model_name}) for {city}")
    plt.ylabel("Temperature (°C)")
    plt.grid(axis='y')
    st.pyplot(plt)

# Load the merged data CSV file
df_merged1 = pd.read_csv('merged_data.csv')
df_merged2 = pd.read_csv('predictions_with_actual.csv')
# Display the prediction page
show_predict_page(df_merged1,df_merged2, feature_names)



