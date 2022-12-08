## Create virtual environment and activate
$ pip -m venv environment_name
## Setup
Install requirements
````
$ pip install -r requirements.txt
````
## Configure the database
````
$ python manage.py migrate
````
## Start the project
In order to start this project you will need to have running Django and Scrapyd at the same time in seprate shell.

In order to run Django
````
$ python manage.py runserver
````
In order to run Scrapyd
````
$ cd scrapy_app
$ scrapyd
````

````

Django is running on: http://localhost:8000
Scrapyd is running on: http://localhost:6800


At this point you will be able to send job request to Scrapyd. This project is setup with a demo spider from the oficial tutorial of scrapy. To run it you must send a http request to Scrapyd with the job info
````
curl http://localhost:6800/schedule.json -d project=default -d spider=toscrape-css
````
## if above command returns "Invoke-WebRequest"
run  remove-item alias:\curl and try again above curl
The crawled data will be automatically be saved in the Django models
