from src.utils.request import get_text
import json

with open(r'src/data/area.txt') as file_obj:
    areas = file_obj.read().split()


def is_location(msg: str, areas: list) -> str:
    for area in areas:
        area = area[:-1] if (len(area) > 2) else area
        if area in msg:
            return area
    return None


async def get_now_weather(area: str, key: str):
    # 获取地区id
    location_url = 'https://geoapi.qweather.com/v2/city/lookup'
    location_params = {
        'key': key,
        'location': area
    }
    data = json.loads(
        await get_text(location_url, params=location_params))
    # 获取实时天气
    now_weather_url = 'https://devapi.qweather.com/v7/weather/now'
    now_weather_params = {
        'key': key,
        'location': data['location'][0]['id']
    }
    data = json.loads(
        await get_text(now_weather_url, params=now_weather_params))
    if data['code'] != 200:
        return data['now']
    else:
        return None


async def get_tomorrow_forcast(area: str, time: str, key: str):
    # 获取地区id
    location_url = 'https://geoapi.qweather.com/v2/city/lookup'
    location_params = {
        'key': key,
        'location': area
    }
    data = json.loads(
        await get_text(location_url, params=location_params))
    # 获取明日预报
    tomorrow_weather_url = 'https://devapi.qweather.com/v7/weather/3d'
    tomorrow_weather_params = {
        'key': key,
        'location': data['location'][0]['id']
    }
    data = json.loads(
        await get_text(tomorrow_weather_url, params=tomorrow_weather_params))
    if data['code'] != 200:
        return data['daily'][0] if time == '今日' else data['daily'][1]
    else:
        return None
