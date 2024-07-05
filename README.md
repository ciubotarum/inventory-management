# Inventory Management Project

## Set Up the environment to Create and Run the Project

Ensure that pyrhon is installed:
`python --version`

Create a Virtual Environment
`python -m venv .venv`

Activate the virtual environment on Windows
`.\.venv\Scripts\Activate.ps1`
# or type `pipenv shell`

Install Django
`pip install Django`

Generate a list of all the installed Python packages and their respective versions and save
`pytho -m pip freeze > requirements.txt`

To set up the project and install the same versions
`py -m pip install -r .\requirements.txt`

Create project named myproject
`django-admin startproject myproject`

Create an application
`python manage.py startapp myapp`

Run server
`python manage.py runserver` 
