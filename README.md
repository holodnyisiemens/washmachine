# Landing page using Django

## Local:

1) Clone repository: with HTTPS - `git clone https://github.com/holodnyisiemens/washmachine.git` | with SSH - `git clone git@github.com:holodnyisiemens/washmachine.git`

2) Change directory: `cd washmachine`

3) Create virtual environment: Windows - `python -m venv djenv` | Linux - `python3 -m venv djenv`

4) Activete virtual environment: Windows - `djenv\Scripts\activate` | Linux - `source djenv/bin/activate`

5) Install packages: Windows - `pip install -r requirements.txt` | Linux - `pip3 install -r requirements.txt`

7) Create file with environment variables: Windows - `Copy-Item .env.template .env` | Linux - `cp .env.template .env`

8) Add your SECRET_KEY in *.env*

9) Create environment variables: Linux using bash - `while read file; do export "$file"; done < .env`

10) Change directory: `cd stirremont`

11) Make migrations for database: Windows - `python manage.py makemigrations` | Linux - `python3 manage.py makemigrations`

12) Apply migrations: Windows - `python manage.py migrate --run-syncdb` | Linux - `python3 manage.py migrate --run-syncdb`

13) Fill in database

14) Run application: Windows - `python manage.py runserver` | Linux - `python3 manage.py runserver`

## PythonAnywhere (example for free version):

1) Start console in *Consoles*

2) Clone repository: with HTTPS - `git clone https://github.com/holodnyisiemens/washmachine.git` | with SSH - `git clone git@github.com:holodnyisiemens/washmachine.git`

3) Change directory: `cd washmachine`

4) Create virtual environment: `python -m venv djenv`

5) Activete virtual environment: `source djenv/bin/activate`

6) Install packages: Windows - `pip install -r requirements.txt`

7) Install dotenv: `pip install python-dotenv`

8) Create file with environment variables: `cp .env.template .env`

9) Add your SECRET_KEY in *.env* using editor. Example `nano .env`

10) In settings.py replace `ALLOWED_HOSTS = ['*']` with `ALLOWED_HOSTS = ['your_account_name.pythonanywhere.com']` using editor. Example: `nano stirremont/stirremont/settings.py`

11) Make migrations for database: `python stirremont/manage.py makemigrations`

12) Apply migrations: `python stirremont/manage.py migrate --run-syncdb`

13) Collect static files: `python stirremont/manage.py collectstatic`

14) In *Files* section in directory */home/your_account_name/washmachine/stirremont* replace *db.sqlite3* with a complete database

15) Fill in *Source code*: */home/your_account_name/washmachine/stirremont*

16) Fill in *Working directory*: */home/your_account_name/washmachine*

17) Edit *WSGI configuration file* using example *py_anywhere_wsgi.py.example* in working directory

18) Select *Virtualenv*: */home/your_account_name/washmachine/djenv*

19) Fill in *Static files*: URL - */static/*, Directory - */home/your_account_name/washmachine/static/*

20) Start website