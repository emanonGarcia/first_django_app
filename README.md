# first_django_app

Loading .csv data into a SQL db using Django migrations

## Summary

This project is an adaptation of an earlier project [The Invincibles](https://github.com/emanonGarcia/invisibles).

## Requirements

[Postgres](http://postgresapp.com/) and [Postico](https://eggerapps.at/postico/) for database management

Python3

```
pip install python3
```

The remaining dependencies are in the requirements.txt

```
pip install -r requirements.txt
```

# Installing

Before running any migrations to your own database make the appropriate changes settings.py

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database name>',
        'USER': '<your username>',
        'PASSWORD': '<your password>',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
'''

After this, from the same directory as manage.py run

```
python manage.py makemigrations
```

followed by

```
python manage.py migrate
```

And you should be g2g. Now go get a pint and chant "There's only team in London!!"

## Author
* *L. Garcia*  - *Initial work* - [emanonGarcia](https://github.com/emanonGarcia)
