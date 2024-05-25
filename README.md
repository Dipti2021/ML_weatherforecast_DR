# ML Weather Forecast

ML Weather Forecast is a web application built with Streamlit that allows users to predict weather conditions based on machine learning models.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## About

This project aims to provide users with a simple interface for weather prediction using machine learning algorithms. The application utilizes Streamlit, a Python library for creating interactive web apps, to visualize and present the weather prediction models.

## Features

## Features

- Predict weather conditions based on input parameters such as temperature, humidity, wind speed, cloudiness, and pressure.
- Choose from a list of top 20 cities in Canada for weather prediction.
- Display actual temperature data retrieved from an external weather API (Open Weather Map).
- Compare predictions from different machine learning models.
- Utilizes Pandas DataFrames for data manipulation and preprocessing.
- Implements machine learning models including Polynomial Regression and Random Forest Regression.
- Uses algorithms such as RNN for weather prediction.

## Usage

To use the ML Weather Forecast app, follow these steps:

1. Clone the repository: git clone https://github.com/Dipti2021/ml-weather-forecast.git
2. Install the required dependencies: pip install -r requirements.txt
3. Run the Streamlit app: streamlit run streamlit_app.py
4. Access the app in your web browser at `http://localhost:8501`.

## Dependencies

The ML Weather Forecast app relies on the following Python libraries:

- Streamlit
- Pandas
- Requests
- Scikit-learn

These dependencies are listed in the `requirements.txt` file and can be installed using pip.

## Contributing

Contributions to ML Weather Forecast are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/yourfeature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/yourfeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
