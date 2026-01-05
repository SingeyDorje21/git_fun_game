import os

API_KEY = os.getenv("API_KEY")


def get_weather(city):
    return f"Sunny in {city}"


print(get_weather("Thimphu"))
