
## Installation(django-backend):

### Preparing the workspace

It's recommended to use venv or other virtualization to maintain python env, ie: [venv](https://docs.python.org/3/library/venv.html).

```shell
# create
python3 -m venv ./.venv/

# activate
. .venv/bin/activate

# check env
which python
# /.venv/bin/python
python --version
# Python 3.9.9
```

### Install Dependencies

```shell
pip install -r requirements.txt
```


## First time setup (django-backend):

When running the application for the first time ensure you've run migrations and created superuser.

### Running migrations
```shell
# in your virtualenv, run:
python manage.py migrate
```

### Creating Super User

```shell
# Provide the details to create the superuser.
python manage.py createsuperuser
```

### Running the server

```shell
python manage.py runserver
```

At this point, you should be able to log into the admin page with the superuser credentials.

Visit: `http://127.0.0.1:8000/admin`

## Running the Django Backend

1. make sure you are in the backend.
2. make sure you are in virtualenv that you created (I name mine: myenv)
3. If not, run "source ./myenv/scripts/activate
4. then run the command: "python manage.py runserver"
