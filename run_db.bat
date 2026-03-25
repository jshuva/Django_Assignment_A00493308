call .venv\Scripts\activate.bat
python manage.py makemigrations api
python manage.py migrate
python populate.py
