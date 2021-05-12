## Extraction of financial data using Django REST Framework
After you downloaded csv files from finance.yahoo.com with all data you should do next steps:

- Extract data to DB by running this script "export_to_db.py" for each csv file.
(In each csv file don't forget to delete space between 'AdjClose')
- activate venv:
`.\env\Scripts\activate`
- install requirements:
`pip install -r requirements.txt`
- create migrations:
`python manage.py makemigrations`
- migrate:
`python manage.py migrate`
- create admin:
`python manage.py createsuperuser`
- run project:
`python manage.py runserver`

worked links:
http://127.0.0.1:8000/api/company/
http://127.0.0.1:8000/api/company/cldr
http://127.0.0.1:8000/api/company/docu
http://127.0.0.1:8000/api/company/pd
http://127.0.0.1:8000/api/company/pins
http://127.0.0.1:8000/api/company/run
http://127.0.0.1:8000/api/company/zm
http://127.0.0.1:8000/api/company/zuo

PS: There is no PVTL company because I didn't find it on finance.yahoo.com:)