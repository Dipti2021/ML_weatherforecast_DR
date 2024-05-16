import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    return pd.read_csv('weather_forecast.csv')

def show_explore_page():
    st.title("Explore Weather Data")
    st.write("This page allows you to explore the weather data.")

    # Load data
    try:
        df = load_data()
    except FileNotFoundError:
        st.error("Data file not found. Please make sure the file exists.")
        return
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return

    # Display some data
    st.write(df)

    # Add visualization or exploration features as needed

    # Plot histograms for numerical columns
    st.subheader("Histograms")
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    for col in numerical_cols:
        st.write(f"### {col} Histogram")
        fig, ax = plt.subplots()  # Create a figure and axis object
        ax.hist(df[col])  # Plot histogram
        ax.set_xlabel(col)  # Set x label
        ax.set_ylabel("Frequency")  # Set y label
        st.pyplot(fig)  # Pass the figure object to st.pyplot()

    # Plot temperature vs. humidity scatter plot
    st.subheader("Temperature vs. Humidity (Scatter Plot)")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='Temperature', y='Humidity', hue='City', ax=ax)
    ax.set_xlabel("Temperature (Fahrenheit)")  # Set x label
    ax.set_ylabel("Humidity (%)")  # Set y label
    ax.set_title("Temperature vs. Humidity")  # Set title
    st.pyplot(fig)

    # Plot temperature over time for each city
    st.subheader("Temperature Over Time (Line Plot)")
    for city in df['City'].unique():
        city_data = df[df['City'] == city]
        plt.plot(city_data['Date'], city_data['Temperature'], label=city)
    plt.xlabel("Date")  # Set x label
    plt.ylabel("Temperature (Fahrenheit)")  # Set y label
    plt.title("Temperature Over Time")  # Set title
    plt.legend()  # Show legend
    st.pyplot(fig)

    # Plot temperature for any 10 cities
    st.subheader("Temperature Comparison for 10 Cities")
    selected_cities = st.multiselect("Select cities", df['City'].unique(), default=df['City'].unique()[:10])
    selected_data = df[df['City'].isin(selected_cities)]
    fig, ax = plt.subplots(figsize=(10, 6))
    for city in selected_cities:
        city_data = selected_data[selected_data['City'] == city]
        ax.plot(city_data['Date'], city_data['Temperature'], label=city)
    ax.set_xlabel("Date")  # Set x label
    ax.set_ylabel("Temperature (Fahrenheit)")  # Set y label
    ax.set_title("Temperature Comparison for Selected Cities")  # Set title
    ax.legend()  # Show legend
    st.pyplot(fig)

 

if __name__ == "__main__":
    show_explore_page()
