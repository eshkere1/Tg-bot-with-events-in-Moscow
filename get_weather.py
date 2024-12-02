from meteostat import Point, Daily
from datetime import datetime
import numpy as np


def get_weather_report(date_input):
    latitude = 55.7522
    longitude = 37.6156
    date = datetime.strptime(date_input.text, "%Y-%m-%d")
    location = Point(latitude, longitude)
    data = Daily(location, date, date).fetch()
    if data.empty:
        return "Данные о погоде не найдены для указанного местоположения и даты."
    min_temp = data["tmin"].iloc[0]
    max_temp = data["tmax"].iloc[0]
    precipitation = data["prcp"].iloc[0]
    result = f"Минимальная температура: {min_temp} °C\n"
    result += f"Максимальная температура: {max_temp} °C\n"
    if np.isnan(precipitation):
        result += "Осадки не наблюдаются"
    else:
        result += f"Осадки: {precipitation} мм"

    return result
