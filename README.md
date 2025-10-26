```markdown
# Tudu

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Tudu is a simple, responsive task / to‑do web application built with Django for the backend and Bootstrap for the frontend. It focuses on fast task management with a clean UI and small, easy-to-understand codebase.

Project snapshot
- Backend: Django (project directory: `tudu`, app: `task`)
- Frontend: HTML/CSS with Bootstrap (templates in `templates`, static files served from `staticfiles`)
- Entry point: `manage.py`
- Other helpers: `requirements.txt`, `Procfile` (for Heroku-like deployment), `build.sh` (build helper)

Features
- Create, edit, and delete tasks
- Mark tasks as complete/incomplete
-Point for complete task
-Pusnish ponint for late complete
-Detect Delayed task and mark them 
- Leaderboard
-Profile view


Table of Contents
- Tech stack
- Requirements
- Quick start (development)
- Running locally
- Database migrations
- Static files & assets
- Screenshots
- Production / deployment notes
- Project structure
- Contributing
- License
- Contact

Tech stack
- Python 3.12.4
- Django
- Bootstrap (CSS framework)
- PostgreSQL (recommended for production)
- Gunicorn (recommended for production)
- Heroku-compatible Procfile included

Requirements
- Python 3.12.4
- pip
- virtualenv or venv
- Git
- PostgreSQL (optional; SQLite works for quick local setups)

Quick start (development)
1. Clone the repository
```bash
git clone https://github.com/Md-Nazmus-Shakib/tudu.git
cd tudu
```

2. Create and activate a virtual environment
```bash
# Linux / macOS
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install Python dependencies
```bash
pip install -r requirements.txt
```

4. Prepare environment variables
Create a file named `.env` in the project root (or set environment variables directly). At minimum set:
```
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3   # or your database URL for production
```
(Consider committing a `.env.example` without secrets to show required keys)

Running locally
1. Apply migrations and create a superuser (optional)
```bash
python manage.py migrate
python manage.py createsuperuser
```

2. Collect static files (for production-like behavior)
```bash
python manage.py collectstatic
```

3. Run the development server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ to see Tudu in action.

Database migrations
- When you add/change models, create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Static files & assets
- Static files are expected under `staticfiles` (project already contains this directory).
- For production, run `python manage.py collectstatic` and serve static files with a webserver (nginx) or via a CDN.
- If you have build steps for CSS/JS, run `./build.sh` (a helper script is included; review it and adapt as needed).

Screenshots
---------
Below are the screenshots for Tudu. To render them in this README, add the image files to the repository at `docs/screenshots/` with the exact filenames used below.
<h1>Landing Page</h1>
<p align="center">
  <img src="https://github.com/Md-Nazmus-Shakib/tudu/blob/main/Screenshot%202025-10-26%20175712.png" alt="Tudu - Landing / Hero" width="1100" />
</p>

<h1>Dashboard</h1>
<p align="center">
  <img src="https://github.com/Md-Nazmus-Shakib/tudu/blob/main/Screenshot%202025-10-26%20180124.png" alt="Tudu - Dashboard filters and stats" width="1100" />
</p>

<h1>Task List</h1>
<p align="center">
  <img src="https://github.com/Md-Nazmus-Shakib/tudu/blob/main/Screenshot%202025-10-26%20180242.png" alt="Tudu - Task list view" width="1100" />
</p>

<h1>Profile</h1>h
<p align="center">
  <img src="https://github.com/Md-Nazmus-Shakib/tudu/blob/main/Screenshot%202025-10-26%20180343.png" alt="Tudu - Task list view" width="1100" />
</p>

<h1>LeaderBoard</h1>
<p align="center">
  <img src="https://github.com/Md-Nazmus-Shakib/tudu/blob/main/Screenshot%202025-10-26%20182722.png" alt="Tudu - Task list view" width="1100" />
</p>

<h1>Task Detail/complete/edit/delete</h1>
<p align="center">
  <img src="https://github.com/Md-Nazmus-Shakib/tudu/blob/main/Screenshot%202025-10-26%20183350.png" alt="Tudu - Task list view" width="1100" />
</p>

<h1>Create Task</h1>
<p align="center">
  <img src="https://github.com/Md-Nazmus-Shakib/tudu/blob/main/Screenshot%202025-10-26%20193600.png" alt="Tudu - Task list view" width="1100" />
</p>

<h1>Edit Task</h1>
<p align="center">
  <img src="https://github.com/Md-Nazmus-Shakib/tudu/blob/main/Screenshot%202025-10-26%20183456.png" alt="Tudu - Task list view" width="1100" />
</p>

How to add the screenshots
1) Using git (recommended)
```bash
mkdir -p docs/screenshots
# copy your images into docs/screenshots as:
# screenshot-1.png, screenshot-2.png, screenshot-3.png

git add docs/screenshots/screenshot-1.png docs/screenshots/screenshot-2.png docs/screenshots/screenshot-3.png
git commit -m "Add README screenshots"
git push origin your-branch
```

2) Using GitHub web
- In the repo, click "Add file" → "Upload files"
- Upload the three images into a new folder `docs/screenshots/`
- Commit the change

Tips
- Use the exact filenames above so the README references render correctly.
- Resize images to a reasonable width (max ~1200px) and optimize file sizes before committing.
- If you prefer one combined image instead of three separate files, upload it and update the image path accordingly.

Production / deployment notes
- A `Procfile` is included to help deploy to platforms like Heroku:
```
web: gunicorn tudu.wsgi --log-file -
```
- Ensure environment variables (SECRET_KEY, DEBUG=False, ALLOWED_HOSTS, DATABASE_URL) are set in the production environment.
- Use PostgreSQL (or another production-grade DB) instead of SQLite for production.
- Use HTTPS in production and a secure configuration for SECRET_KEY and allowed hosts.

Project structure (high level)
- manage.py                   — Django management entrypoint
- requirements.txt            — Python dependencies
- Procfile                    — example process file for Heroku
- build.sh                    — helper build script
- tudu/                       — Django project settings, wsgi, urls
- task/                       — the Django app that contains models, views, forms (task logic)
- templates/                  — HTML templates (Bootstrap-based)
- staticfiles/                — CSS/JS/images and other static assets
- docs/screenshots/           — recommended location for README screenshots
- README.md                   — this file

Contributing
Contributions are welcome. Suggested workflow:
1. Fork the repository
2. Create a feature branch: git checkout -b feature/your-feature
3. Commit your changes with descriptive messages
4. Open a pull request describing the intent and tests performed

Please follow PEP8 and keep front-end markup accessible and responsive. Add tests for new or changed behavior wherever possible.

Testing
- If tests are added (Django's test framework), run:
```bash
python manage.py test
```
- Add unit tests for models and views to keep regressions low.

Security & configuration tips
- Never commit real SECRET_KEY or database credentials to the repository.
- Use environment variables or secrets management provided by your hosting platform.
- Set DEBUG=False in production and populate ALLOWED_HOSTS.

License
This project does not include a LICENSE file by default. If you want to make the project open source, add a LICENSE (MIT recommended) to the repository.

Contact
Maintainer: Md-Nazmus-Shakib  
GitHub: https://github.com/Md-Nazmus-Shakib

Acknowledgements
- Built with Django and Bootstrap.
- Thanks to contributors and open-source libraries used in this project.
```
