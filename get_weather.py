from meteostat import Point, Daily
from datetime import datetime

def get_user_input(date_input="2024-11-30"):
    try:
        date = datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Неверный формат даты. Попробуйте снова.")
    return latitude, longitude, date

def fetch_weather_data(latitude, longitude, date):
    location = Point(latitude, longitude)
    data = Daily(location, date, date)
    return data.fetch()

def display_weather_data(data):
    if not data.empty:
        min_temp = data['tmin'].iloc[0]
        max_temp = data['tmax'].iloc[0]
        print(f"Минимальная температура: {min_temp} °C")
        print(f"Максимальная температура: {max_temp} °C")
    else:
        print("Данные о погоде не найдены для указанного местоположения и даты.")

def main():
    latitude, longitude, date = get_user_input()
    if not all([latitude, longitude, date]):
        return
    
    data = fetch_weather_data(latitude, longitude, date)
    display_weather_data(data)

if __name__ == "__main__":
    latitude = 55.7522
    longitude = 37.6156
    main()