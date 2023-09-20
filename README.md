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

## What is the difference between `POST` form and `GET` form in Django?
**GET form:**
-   Appends the form data to the URL in a query string.
-   Data is visible in the URL, which means it has limitations on the amount of data that can be sent (due to URL length restrictions).
-   GET is suitable for data retrieval and should not be used for sensitive or confidential information, as the data is visible in the URL.
-   It is cached by browsers and can be bookmarked, making it suitable for search forms or sharing URLs.

**POST form:**
-   Sends the form data in the body of the HTTP request.
-   Data is not visible in the URL, making it suitable for sensitive or large amounts of data.
-   POST does not have limitations on the amount of data that can be sent.
-   It's secure and suitable for actions that modify data on the server (e.g., creating, updating, deleting).

## What are the main differences between XML, JSON, and HTML in the context of data delivery?
XML and JSON are primarily used for data interchange and storage, with JSON being more lightweight and easy to read/write. HTML, on the other hand, is focused on defining the structure and presentation of web content.

## Why is JSON often used in data exchange between modern web applications?
JSON is a popular choice for data exchange in modern web applications due to its simplicity, compatibility with JavaScript, language agnosticism, efficiency, lightweight nature, standardization, and support for complex data structures.

## Assignment Steps #2
-   #### Create a  `form`  input to add a model object to the previous app.
1. Create a new folder named `template` in root directory and add base.html into it with the code:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
2. edit `settings.py` in the `django_inv` folder to detect base.html as a template file
```python
# django_inv/settings.py
...
TEMPLATES = [
	{
		...
		'DIRS':  [BASE_DIR /  'templates'],
		...
	}
]
...
```
3. use base template in `main/templates/main.html` by adding:
```html
{% extends 'base.html' %}
{% block content %}
...
{% endblock content %}
```

4. create new `forms.py` inside the main folder
```python
from django.forms import ModelForm
from main.models import Item

class  ItemForm(ModelForm):
	class  Meta:
		model = Item
		fields =  ["name",  "amount",  "category",  "price",  "description"]
```
5. add items into the `show_main` function in `views.py`
```py
items = Item.objects.all()
context = {
	...
	'items': items
}
```

6. create a new file in `main/templates` directory named `create_item.html`
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
7. add this code to `main.html` to see the item list and a button to create new item:
```html
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Below is how to show the product data {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %} 
```
#### Add 5  `views`  to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.
by adding these to `views.py`
```python
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from main.forms import ItemForm
from main.models import Item
...

...
def  create_item(request):
form =  ItemForm(request.POST  or  None)
	if form.is_valid()  and request.method ==  "POST":
		form.save()
		return  HttpResponseRedirect(reverse('main:show_main'))
context =  {'form': form}
return  render(request,  "create_item.html", context)

def  show_xml(request):
	data = Item.objects.all()
	return  HttpResponse(serializers.serialize("xml", data),content_type="application/xml")

def  show_json(request):
	data = Item.objects.all()
	return  HttpResponse(serializers.serialize("json", data),content_type="application/json")

def  show_xml_by_id(request,  id):
	data = Item.objects.filter(pk=id)
	return  HttpResponse(serializers.serialize("xml", data),content_type="application/xml")

def  show_json_by_id(request,  id):
	data = Item.objects.filter(pk=id)
	return  HttpResponse(serializers.serialize("json", data),content_type="application/json")
```

#### Create URL routing for each of the views added in point 2.
1.  Open the `urls.py` file located in the `main` folder and import the functions.
```py
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
```
2. Add URL paths to the `urlpatterns` list to access the imported functions.
```py
...
path('create_item', create_item,  name='create_item'),
path('xml/', show_xml,  name='show_xml'),
path('json/', show_json,  name='show_json'),
path('xml/<int:id>/', show_xml_by_id,  name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id,  name='show_json_by_id'),
...
```

#### Access the five URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.
<img src="/IMG/json.png"><br />
<img src="/IMG/xml.png"><br />
<img src="/IMG/html.png"><br />
<img src="/IMG/json_id.png"><br />
<img src="/IMG/xml_id.png"><br />