djangomongotestapp
==================

Django Mongoengine Test Application

1. Install MongoDB
2. Create virtualenv and activate it
3. pip install -r requirements.txt
4. By default, app will work with 'test' mongo database (see settings.py)
5. Model of data - timeseriesdata.models.Log
6. Run command:
python manage.py fillsampledata 
This command is adding 1000 new random samples to the database 
7. Run the server:
python manage.py runserver 0.0.0.0:8000
8. API for the data:
http://127.0.0.1:8000/api/v1/timeseriesdata/log/?format=json
9. Go to the index url: http://127.0.0.1:8000/
