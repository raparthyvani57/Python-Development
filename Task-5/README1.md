Weather App with OpenWeather API
Project Overview

This project is a Python weather application that uses the OpenWeather API to fetch real-time weather information for a city entered by the user.

Features
Real-time weather information
Temperature in Celsius
Feels-like temperature
Humidity
Weather condition
Wind speed
Tkinter graphical user interface
REST API integration using Requests
JSON response parsing
Error handling
Secure API key storage using a .env file
Technologies Used
Python
Requests
Tkinter
OpenWeather API
JSON
python-dotenv
How It Works
The user enters a city name.
The application sends a request to the OpenWeather API.
The API returns weather information in JSON format.
Python parses the JSON response.
The application displays the weather information in the Tkinter interface.
Installation

Install the required packages:

pip install -r requirements.txt

API Key Setup

Create a .env file in the project folder and add:

OPENWEATHER_API_KEY=your_api_key_here


Do not upload the .env file to GitHub.

Running the Application

Run:

python Weatherapp.py


Enter a city name and click Get Weather.

Example

The application can display:

City and country
Temperature
Feels-like temperature
Humidity
Weather condition
Wind speed
Conclusion

This project demonstrates how Python can connect to a real-world cloud API, process JSON data, and display live information through a graphical user interface.