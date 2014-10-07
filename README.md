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
