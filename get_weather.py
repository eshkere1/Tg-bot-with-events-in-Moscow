from meteostat import Point, Daily
from datetime import datetime
import numpy as np


def get_weather_report(date_input):
    latitude = 55.7522
    longitude = 37.6156
    try:
        date = datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        return "Неверный формат даты. Используйте формат ГГГГ-ММ-ДД."
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


if __name__ == "__main__":
    date_input = "2024-11-30"  # Пример даты
    report = get_weather_report(date_input)
    print(report)
