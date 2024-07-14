import logging
import requests
import asyncio
import schedule
import json
import time
import telegram

from config import config
from db import session, Weather

##### Telegram API #####
telegram_token = config.TELEGRAM_TOKEN
channel_id = config.CHANNEL_ID

##### OpenWeatherMap API #####
city = config.CITY
country_code = config.COUNTRY_CODE
measurement = config.MEASUREMENT
api_key_weather = config.API_KEY_WEATHER
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key_weather}&units={measurement}"

def get_weather_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print (data)
            return data
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def filter_weather_data(data):
    main_data = data["main"]
    weather_data = data["weather"][0]
    location_data = data["sys"]

    temperature = main_data["temp"]
    feels_like = main_data["feels_like"]
    humidity = main_data["humidity"]
    description = weather_data["description"]
    country = location_data["country"]
    town = data["name"]
    jsonfile = {
        "temperature": round(temperature, 1),
        "humidity": humidity,
        "description": description,
        "feels_like": feels_like,
        "country": country,
        "city": town,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
    return jsonfile, temperature, humidity, description, country, town, feels_like

def database_upload(temperature,humidity,description,country,town,feels_like):
    new_data = Weather(temperature=temperature,
                       humidity=humidity,
                       description=description,
                       country=country,
                       feels_like=feels_like,
                       town=town)
    session.add(new_data)
    session.commit()
    session.close()

##### Sending_Data_To_TelegramUser #####
async def send_data(jsonfile):
    bot = telegram.Bot(token=telegram_token)
    await  bot.send_message(chat_id=channel_id,text = json.dumps(jsonfile,indent = 6))
def action():
    data = get_weather_data(url)
    if data:
        jsonfile,temperature, humidity, description, country, town, feels_like = filter_weather_data(data)
        database_upload(temperature, humidity, description, country, town ,feels_like)
        asyncio.run(send_data(jsonfile))

##### Schedule_Time_Activation #####
schedule.every().day.at("09:00").do(action)
schedule.every().day.at("19:00").do(action)

if __name__ == "__main__":
    logging.info("Script started")
    while True:
        schedule.run_pending()
        time.sleep(1)
