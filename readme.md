# Weather Bot

This Weather Bot is a Python application that fetches weather data from the OpenWeatherMap API and sends it to a Telegram channel at scheduled times. The data is also stored in a MySQL database.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetches weather data from the OpenWeatherMap API.
- Sends weather updates to a specified Telegram channel.
- Stores weather data in a MySQL database.
- Schedules tasks to run at specific times daily.

## Requirements

- Python 3.8 or higher
- MySQL
- Telegram Bot API token
- OpenWeatherMap API key

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/weather-bot.git
    cd weather-bot
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the project directory and add your configuration variables:

    ```env
    TELEGRAM_TOKEN=your_telegram_token
    CHANNEL_ID=your_channel_id
    CITY=your_city
    COUNTRY_CODE=your_country_code
    MEASUREMENT=metric_or_imperial
    API_KEY_WEATHER=your_openweathermap_api_key
    MYSQL_DATABASE=your_mysql_database
    MYSQL_USER=your_mysql_user
    MYSQL_PASSWORD=your_mysql_password
    MYSQL_HOST=your_mysql_host
    ```

2. Update the `config.py` file to use these environment variables:

    ```python
    from pydantic_settings import BaseSettings

    class Settings(BaseSettings):
        TELEGRAM_TOKEN: str
        CHANNEL_ID: int
        CITY: str
        COUNTRY_CODE: str
        MEASUREMENT: str
        API_KEY_WEATHER: str
        MYSQL_DATABASE: str
        MYSQL_USER: str
        MYSQL_PASSWORD: str
        MYSQL_HOST: str

        class Config:
            env_file = ".env"
            env_file_encoding = "utf-8"

    config = Settings()
    ```

## Usage

1. Run the script:

    ```sh
    python main.py
    ```

2. The script will fetch weather data and send updates to the specified Telegram channel at the scheduled times (09:00 and 19:00).

## Deployment

### PythonAnywhere

1. Upload your project files to PythonAnywhere.

2. Set up a virtual environment on PythonAnywhere:

    ```sh
    mkvirtualenv --python=python3.10 your_virtualenv_name
    ```

3. Install the required packages in the virtual environment:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your MySQL database on PythonAnywhere.

5. Configure the environment variables on PythonAnywhere:

    - Go to the "Web" tab.
    - Scroll down to "Virtualenv" section and specify the path to your virtual environment.
    - In the "Code" section, set the working directory to your project folder.
    - In the "Static files" section, map the URL `/static/` to the path `your_project_folder/static/`.

6. Set up an always-on task:

    - Go to the "Tasks" tab.
    - Add a new task with the command to run your script:

    ```sh
    /path/to/your/virtualenv/bin/python /home/yourusername/your_project_folder/main.py
    ```

7. Check the logs if the script is running as expected.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
