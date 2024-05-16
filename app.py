import streamlit as st
from predict import show_predict_page
from explore import show_explore_page
# import joblib


def main():
    st.sidebar.title("Weather Prediction App")
    page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

    if page == "Predict":
        show_predict_page()
    else:
        show_explore_page()

if __name__ == "__main__":
    main()
