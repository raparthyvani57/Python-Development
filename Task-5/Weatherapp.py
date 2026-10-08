import requests
import os
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Required", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        result_label.config(
            text=(
                f"📍 {city_name}, {country}\n\n"
                f"🌡 Temperature: {temperature} °C\n"
                f"🌡 Feels Like: {feels_like} °C\n"
                f"💧 Humidity: {humidity}%\n"
                f"☁ Weather: {description.title()}\n"
                f"🌬 Wind Speed: {wind_speed} m/s"
            )
        )

    except requests.exceptions.HTTPError as error:
        if response.status_code == 404:
            messagebox.showerror(
                "City Not Found",
                "Please check the city name and try again."
            )
        elif response.status_code == 401:
            messagebox.showerror(
                "API Key Error",
                "Your OpenWeather API key is not active yet."
            )
        else:
            messagebox.showerror(
                "API Error",
                f"HTTP Error: {response.status_code}"
            )

    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Network Error",
            "Could not connect to the weather service."
        )

    except (KeyError, TypeError):
        messagebox.showerror(
            "Data Error",
            "Unexpected data was received from the API."
        )


# Create main window
window = tk.Tk()
window.title("Weather App")
window.geometry("500x500")
window.resizable(False, False)
window.configure(bg="#EAF4FF")


# Title
title_label = tk.Label(
    window,
    text="🌤 Weather App",
    font=("Arial", 26, "bold"),
    bg="#EAF4FF",
    fg="#1769AA"
)

title_label.pack(pady=25)


# Instructions
instruction_label = tk.Label(
    window,
    text="Enter a city name to get live weather",
    font=("Arial", 12),
    bg="#EAF4FF",
    fg="#444444"
)

instruction_label.pack(pady=5)


# City input
city_entry = tk.Entry(
    window,
    font=("Arial", 16),
    width=25,
    justify="center"
)

city_entry.pack(pady=15)


# Search button
search_button = tk.Button(
    window,
    text="Get Weather",
    font=("Arial", 13, "bold"),
    bg="#1769AA",
    fg="white",
    padx=20,
    pady=8,
    command=get_weather
)

search_button.pack(pady=10)


# Result area
result_label = tk.Label(
    window,
    text="Weather information will appear here.",
    font=("Arial", 14),
    bg="white",
    fg="#222222",
    width=40,
    height=10,
    relief="groove",
    justify="center"
)

result_label.pack(pady=25)


# Start application
window.mainloop()