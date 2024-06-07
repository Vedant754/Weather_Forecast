import requests
from config import API_KEY, BASE_URL, FORECAST_URL

def fetch_weather(city):
    try:
        complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}

def fetch_forecast(city):
    try:
        complete_url = f"{FORECAST_URL}q={city}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}
