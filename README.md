# Inventory Management Project

## Set Up the Environment to Create and Run the Project

### Prerequisites

1. Ensure that Python is installed:
    ```sh
    python --version
    ```

2. Create a Virtual Environment:
    ```sh
    python -m venv .venv
    ```

3. Activate the Virtual Environment:
    - On Windows:
      ```sh
      .\.venv\Scripts\Activate.ps1
      ```
    - Or type:
      ```sh
      pipenv shell
      ```

4. Install Django:
    ```sh
    pip install Django
    ```

5. Generate a List of All Installed Python Packages and Their Respective Versions, and Save to `requirements.txt`:
    ```sh
    python -m pip freeze > requirements.txt
    ```

6. Set Up the Project and Install the Same Versions:
    ```sh
    pip install -r requirements.txt
    ```

7. Create a Django Project Named `myproject`:
    ```sh
    django-admin startproject myproject
    ```

8. Create an Application Named `myapp`:
    ```sh
    python manage.py startapp myapp
    ```

9. Run the Development Server:
    ```sh
    python manage.py runserver
    ```

## Additional Information

- **Make Migrations**:
  - To apply migrations for db
    ```sh
    python manage.py makemigrations
    ```

- **Running Migrations**:
  - To apply migrations and create the necessary database tables, run:
    ```sh
    python manage.py migrate
    ```

- **Instantiate Tour Class**:
  - To create Tour objects, records in our db (go to `python manage.py shell`):
    ```sh
    from asiatoursagency.models import Tour

    to1 = Tour(origin_country="Japan", destination_country="China", number_of_nights=10, price=1500)
    ```
  - To save the tour in database
    ```sh
    to1.save()
    ```

- **Creating a Superuser**:
  - To create a superuser account for accessing the Django admin interface, run:
    ```sh
    python manage.py createsuperuser
    ```

