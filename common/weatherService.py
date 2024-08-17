import requests


class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.weatherapi.com/v1"

    def get_current_weather(self, city):
        url = f"{self.base_url}/current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "temperature": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"]
            }
        else:
            raise Exception("Failed to get weather data")
