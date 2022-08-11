import json
import requests


def Weather(city):
    api_address = 'http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=011c815dce7772f853b2fb12180d8355'
    url = api_address + city

    json_data = requests.get(url).json()
    format_add = json_data['main']
    print(format_add)
    return format_add
