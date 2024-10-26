# Plant Watering Schedule API

This project provides a simple API to manage a Plant Watering Schedule using Django Rest Framework. The API allows users to create, retrieve, and update information about plants, including their watering schedules.

# Installing using GitHub
Follow these steps to set up the project locally:


Clone the repository and switch to the project directory:
```shell
git clone https://github.com/AntonKorinchuk/Plant-Watering-Schedule-API.git
cd plant_watering_schedule_api
```

Create a virtual environment:
```shell
python -m venv venv
```

Activate the virtual environment:
On Windows:
```shell
 venv\Scripts\activate
 ```
On macOS and Linux:
```shell
source venv/bin/activate
```

Install dependencies:
```shell
pip install -r requirements.txt
```

Apply migrations:
```shell
python manage.py migrate
```
### Rename .env.template to .env file and populate it with the required data

Run:
```shell
python manage.py runserver
```