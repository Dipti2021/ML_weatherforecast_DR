import streamlit as st
import pandas as pd
from predict import show_predict_page
from explore import show_explore_page

def main():
    st.sidebar.title("Weather Prediction App")
    page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

    if page == "Predict":
        # Load DataFrame for prediction
        df_predict = pd.read_csv('merged_data.csv')
        show_predict_page(df_predict, ['Temperature', 'Humidity', 'Wind Speed', 'Cloudiness', 'Pressure'])
    else:
        # Load DataFrame for exploration
        df_explore = pd.read_csv('weather_forecast.csv')  # Load original weather forecast data
        show_explore_page(df_explore)

        # # Load DataFrame for exploration (merged data)
        # df_merged_explore = pd.read_csv('merged_data.csv')  # Load merged data
        # show_explore_page(df_merged_explore)

if __name__ == "__main__":
    main()
