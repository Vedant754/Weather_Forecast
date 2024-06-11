# Weather Forecast App

## Description
This Weather App allows users to get current weather information for various states in India. It uses the OpenWeather API to fetch the data and display it in a user-friendly interface. The app also provides a 5-day weather forecast, search history, and favorite cities functionality.

## Features
- Fetch current weather information
- Display weather climate, description, temperature, pressure, humidity, and wind speed
- Show a 5-day weather forecast with a graphical representation
- Maintain search history and favorite cities
- Responsive and user-friendly UI
- Loading indicator while fetching data

## Project Structure
weather_app/
<br>
|-- main.py            # Entry point of the application
<br>
|-- ui.py              # Contains the UI code
<br>
|-- weather_api.py     # Contains the API call functions
<br>
|-- config.py          # Configuration file for API keys and base URLs
<br>
|-- utils.py           # Utility functions for graphical representation
<br>
|-- README.md          # Project documentation
<br>
|-- requirements.txt   # List of required Python packages


## Installation

### Prerequisites
- Python 3.7 or higher
- An OpenWeather API key (you can get one by signing up on the [OpenWeather website](https://home.openweathermap.org/users/sign_up))

### Steps

1. **Clone the repository:**
   First, clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   Replace "yourusername" with your actual GitHub username.
2. **Navigate to the project directory:**
   cd weather-app
3. **Install the required packages:**
   pip install -r requirements.txt
4. **Configure the API key:**
   Open the config.py file in a text editor and replace your_api_key_here with your actual OpenWeather API key:
   <br>
   API_KEY = "your_api_key_here"
   <br>
   BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
   <br>
   FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast?"
6. **Run the application:**
    Finally, start the application by running the main.py file:


