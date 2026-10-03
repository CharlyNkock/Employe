# Employe

Application Django de gestion des employés.

## Description

Ce projet permet de :
- ajouter un employé ;
- lister les employés ;
- afficher les informations principales de chaque employé ;
- gérer les données via l’interface Django admin.

## Stack technique

- Python 3.11
- Django 3.1.3
- SQLite

## Structure du projet

```bash
Employe/
├── employe/
│   ├── templates/
│   │   └── employes/
│   │       ├── base.html
│   │       ├── formulaire.html
│   │       └── list.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── rh/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
├── .gitignore
└── README.md
```

## Prérequis

- Python 3.10 ou plus
- pip

## Installation

1. Cloner le projet :

```bash
git clone https://github.com/CharlyNkock/Employe.git
cd Employe
```

2. Créer un environnement virtuel :

```bash
python -m venv .venv
```

3. Activer l’environnement virtuel :

Windows PowerShell :

```powershell
.\.venv\Scripts\Activate.ps1
```

Windows CMD :

```cmd
.venv\Scripts\activate.bat
```

4. Installer Django :

```bash
pip install django
```

5. Appliquer les migrations :

```bash
python manage.py migrate
```

## Lancement du projet

```bash
python manage.py runserver
```

Puis ouvrir :

```text
http://localhost:8000/
```

## Accès à l’admin

Pour créer un superutilisateur :

```bash
python manage.py createsuperuser
```

Ensuite ouvrir :

```text
http://localhost:8000/admin/
```

## Contribution

Les contributions sont les bienvenues.

## Licence

Ce projet est fourni à titre éducatif.
