# covid-metrics

### Create virtual env folder
`python -m venv project-name\venv`

### Activate virtual env
`. venv\scripts\activate`

### Install packages from requirements.txt (actually not sure what this does)
`pip install -r requirements.txt`

### Generate requirements.txt
`pip freeze > requirements.txt`

### Install package in virtual env and add it to requirements.txt
`pip install psycopg2; pip freeze > requirements.txt`

### De-activate virtual env
`deactivate`
