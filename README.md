# Survey WebApp
> Django based application for performing surveys and tracking user points after completing surveys.

## Overview
A Django based Surveying WebApp with login, and signup feature to track user responses and give them points after completing a survey. 
<br/>
<br/>
The survey can be found on https://github.com/maarouf-yassine/Survey-WebApp--Django
<br/>
<br/>
Users of our application could add and delete Surveys and Categories. 
<br/>
<br/>
After completing a survey, users will gain an extra point, and they be prompted to a report page that summarizes the answers on this specific survey.
<br/>
<br/>
When a user enters a specific category, he/she will be able to see the users that participated in surveys that fall under this category, in addition to viewing their own points.  

## Requirements
To be able to run the Django server, you need to have the following tools on your machine:
```
* Python 3.7+
* Django 3.1.6+
```
Create a virtual environment and add the following commands:
```
> cd /path/to/new/virtual/environment
> python -m venv my_env
> my_env\Scripts\activate
> pip install django 
```

## Run
To run this application, make sure to first be in the correct directtory in your terminal and having django present in your activated virtual environment. Then run:
```
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver
```
