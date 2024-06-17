# Landing page using Django

Use:

1) Clone repository: with HTTPS - `git clone https://github.com/holodnyisiemens/washmachine.git` | with SSH - `git clone git@github.com:holodnyisiemens/washmachine.git`

2) Change directory: `cd washmachine`

3) Create virtual environment: Windows - `python -m venv env` | Linux - `python3 -m venv djenv`

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