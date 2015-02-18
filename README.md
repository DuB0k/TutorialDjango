Tutorial Django1.7 en Pythonanywhere
====================================

[Website](http://dub0k.pythonanywhere.com/)
-------

https://www.pythonanywhere.com/wiki/DjangoTutorial
https://www.pythonanywhere.com/wiki/FollowingTheDjangoTutorial
https://www.pythonanywhere.com/wiki/VirtualEnvForNewerDjango


Entorno virtual
---------------

Django1.7 y python3.3:

`mkvirtualenv django17 --python=/usr/bin/python3.3`
`pip install django`

Compruebo que django se ha instalado correctamente:

`python -c "import django; print(django.get_version())"`

Creo el projecto desde la consola:

`django-admin.py startproject tutorial`

Creo la django app de las encuestas:

`python manage.py startapp polls`


Configuración de la web app
---------------------------

Para utilizar el entorno, no utilizar el asistente sino que creo la web app manualmente.Elijo python3.3 y configuro el entorno virtual creado antes:

`/home/dub0k/.virtualenvs/django17/`

En los ficheros estáticos creo una nueva url:

`/static/admin/`

Y le asigno el siguiente directorio:

`/home/dub0k/.virtualenvs/django17/lib/python3.3/site-packages/django/contrib/admin/static/admin`

Con esto consigo cargar los ficheros css del admin site.


Configracion de wsgi.py
-----------------------
Modifico el fichero creado por defecto con lo siguiente:

`##start custom settings
##http://www.tangowithdjango.com/book17/chapters/deploy.html
# TURN ON THE VIRTUAL ENVIRONMENT FOR YOUR APPLICATION
activate_this = '/home/dub0k/.virtualenvs/django17/bin/activate_this.py'

with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))

import os
import sys

# ADD YOUR PROJECT TO THE PYTHONPATH FOR THE PYTHON INSTANCE
path = '/home/dub0k/tutorial/'
if path not in sys.path:
    sys.path.append(path)

# IMPORTANTLY GO TO THE PROJECT DIR
os.chdir(path)

# TELL DJANGO WHERE YOUR SETTINGS MODULE IS LOCATED
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')

# IMPORT THE DJANGO SETUP - NEW TO 1.7
import django
django.setup()

# IMPORT THE DJANGO WSGI HANDLER TO TAKE CARE OF REQUESTS
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
##end custom settings`


Creacion de la base de datos SQLlite:
-------------------------------------

Modifico el fichero de settings (tutorial/settings.py):

`DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/home/dub0k/tutorial/db.sqlite',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': ''
        }
    }`

Añado la app de las encuestas a la lista de apps en settings.py

Sincronizo la base de datos:

`python manage.py syncdb`

