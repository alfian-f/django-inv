# Django's Inventory
#### Alfian Fadhlurrahman - 2206821683

## Assignment Steps
- #### Create a new Django project.
 I started the Django project by creating a new git repository. after that I initialize the virtual environment by running the command `python -m venv env`, and then activated it with `env\Scripts\activate.bat`. After that, I set up dependencies and started creating the django project by:
1. Creating requirements.txt
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
2. Installing requirements
```bash
pip install -r requirements.txt"
```
3. Create a new django project
```bash
django-admin startproject django_inv .
```
4. Set `ALLOWED_HOST` to any in `settings.py` for deployment purposes
```
...
ALLOWED_HOST = ["*"]
...
```
* #### Create an app with the name main on that project.
	by running `python manage.py startapp main` to create the main application. and then registering it into the project by adding main to INSTALLED_APPS in `settings.py`
```python
# django_inv/settings.py
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
- #### Create a URL routing configuration to access the main app.
by filling `urls.py` **inside** the `main` application directory with:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

- #### Create a model on the main app with name Item and it's attributes:
by filling `models.py` inside `main` with:
```python
from django.db import models

class  Item(models.Model):
	name = models.CharField(max_length=100)
	date_added = models.DateField(auto_now_add=True)
	amount = models.IntegerField()
	description = models.TextField()
	category = models.TextField()
	price = models.IntegerField()
```

- #### Create a function in `views.py` that returns an HTML template containing your application name, your name, and your class.
1. Create a `main.html` in `main/templates`
```html
# main/templates/main.html
<h1>Django's Inventory</h1>

<h5>Name: </h5>
<p>{{ name }}</p>

<h5>Class: </h5>
<p>{{ class }}</p>
```
2. Create the view function in `views.py`
```python
# main/views.py
...
def  show_main(request):
	context =  {
		'name':  'Alfian Fadhlurrahman',
		'class':  'PBP KKI'
	}
		return  render(request,  'main.html', context)
...
```
- #### Create a routing in `urls.py` to map the function in `views.py` to an URL.
filling `urls.py` file **inside** the project's  `django_inv`  directory, not within the  `main`  application.
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns =  [
	path('admin/', admin.site.urls),
	path('main/',  include('main.urls')),
]
```
- #### Deploy your app to Adaptable so it can be accessed through the internet.
My account has been disabled in Adaptable :(

## Flow of Client Requests to a Django Web App 
<img src="IMG/diagram.png">

the flow of client requests to a Django web app invovles routing the request through `urls.py` to the appropriate view function in `views.py`. The view function interacts with the model in `models.py` to retrieve or modify data and then renders an HTML template, which forms the HTTP response sent back to the client for display in the browser.

## Virtual Environment
A virtual environment in software development serves to create isolated and self-contained environments for Python projects, primarily for dependency isolation, version compatibility, and maintaining a clean development environment. While it is technically possible to create a Django web app without a virtual environment, it is strongly discouraged due to potential dependency conflicts, lack of isolation, and reduced portability. Using a virtual environment is highly recommended for Django web app development as it ensures a well-defined and isolated environment, making it easier to manage dependencies, prevent conflicts, and ensure consistent and reproducible project setups across different environments and deployments.

## MVC, MVT, MVVM
**MVC** (Model-View-Controller):
MVC is a pattern that emphasizes the separation of concerns between data, user interface, and control logic. It is commonly used in web applications, desktop applications, and other user-facing software.

**MVT** (Model-View-Template):
MVT is a pattern commonly used in web frameworks like Django (Python) and Ruby on Rails (Ruby). It is similar to MVC but separates the View and Template layers more explicitly for web development.

**MVVM** (Model-View-ViewModel):
MVVM is commonly used in modern front-end and mobile app development, especially with frameworks like Angular (for web apps), Xamarin (for mobile apps), and WPF (Windows Presentation Foundation). It aims to improve the separation of concerns by introducing the ViewModel layer, which simplifies UI development.