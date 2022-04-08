Installation(django-backend):
1. install virtualenv in the backend of entire project
2. go activate virtualenv while in backend and create the virtualenv environment. 
3. install django
4. install install django-REST
5. apply settings to the Settings.py if needed(probably not with this)
6. install django-REST simple-JWT authentication system (in the django-REST authentication system)


First time setup(django-backend):
1. When running the application for the firs time you need to make sure that you have your migrations done and superuser created.
2. in your virtualenv, run "python manage.py migrate" 
3. then you run "python manage.py createsuperuser" and provide the details to create the superuser. This is an important step in deployment, but I would make it something easy when using sqlite
4. afterwhich you can run "python manage.py runserver" and go to your local port that is hosting the site (more than likely 8000) and go to /admin. "http://127.0.0.1:8000/admin" to login with your details and see the admin panel to confirm everything works. 

To Run(django-backend):
1. make sure you are in the backend.
2. make sure you are in virtualenv that you created (I name mine: myenv)
3. If not, run "source ./myenv/scripts/activate
4. then run the command: "python manage.py runserver"
