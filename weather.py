from datetime import datetime
import requests

TOKYO_CODE = 130000


def get_weather(code):
    api_url = f'https://www.jma.go.jp/bosai/forecast/data/forecast/{code}.json'
    weather_data = requests.get(api_url).json()

    area_name = weather_data[0]['timeSeries'][0]['areas'][0]['area']['name']
    time_series = weather_data[0]['timeSeries'][0]['timeDefines']
    weather_series = weather_data[0]['timeSeries'][0]['areas'][0]['weathers']

    weathers = f'{len(time_series)}日間の天気予報\n'
    for time, weather in zip(time_series, weather_series):
        time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S+09:00')
        weathers += f'\t{time}の{area_name}の天気は{weather}です \n'
    else:
        weathers += '\n'

    # def get_weather_detail(code):
    #     api_url = f'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{code}.json'
    #     weather_data = requests.get(api_url).json()
    #     return weather_data['text']
    detail_url = f'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{code}.json'
    weather_data = requests.get(detail_url).json()

    weathers += weather_data['text']

    return weathers


weather_info = get_weather(TOKYO_CODE)
print(weather_info)
