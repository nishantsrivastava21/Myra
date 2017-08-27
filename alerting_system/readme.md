Install  python 2.7.0 or above
install mysql
install pip
create a data base with name myra_data
update username and password in settings.py

clone the repository
intall the applications listed in requirements.txt
pip install -r requirements.txt

navigate to the project repository
run the application using
python manage.py runserver

create super user
python manage.py createsuperuser


Access the admin portal
http://127.0.0.1:8000/admin

Alternatively, navigate to login URL:
127.0.0.1:8000/accounts/login

Login using the username and password

Dashboard will list down all the alerts
Click on Add new Alert and a form will apperar and you can add new alert

Alternatively, you can call the API URL directly,

List Alerts:
http://127.0.0.1:8000/api/v1/alerts/

From the same page you can post a new alert and delete ant alert.


