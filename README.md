# hackathon

[![Python Version](https://img.shields.io/badge/python-3.9-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2.5-brightgreen.svg)](https://djangoproject.com)
[![Django Rest Framework Version](https://img.shields.io/badge/djangorestframework-3.12.4-brightgreen.svg)](https://www.django-rest-framework.org/)


## Running the Project Locally


Click on `Fork`.

Go to your fork and `clone` the project to your local machine.

```bash
git clone https://github.com/Gautamaggrawal/hackathon.git
```

Create and activate virtualenv 

```bash
python3 -m venv env
source env/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The API endpoints will be available at **127.0.0.1:8000**.

