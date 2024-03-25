# Game-Management

![Python Version](https://img.shields.io/badge/python-3.11-blue.svg?style=plastic)
[![Django](https://img.shields.io/badge/django-5.0.3-green.svg?style=plastic)](https://djangoproject.com)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

![Contributors](https://img.shields.io/github/contributors/Computer-Engineering-UdL/Game-Management.svg?style=plastic&color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/Computer-Engineering-UdL/Game-Management?style=plastic&color=lightgreen)
![GitHub issues](https://img.shields.io/github/issues/Computer-Engineering-UdL/Game-Management?style=plastic&color=yellow)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Computer-Engineering-UdL/Game-Management?style=plastic&color=pink)

## Description

[Django](https://www.djangoproject.com/) web application to manage a history of games played.
This project is part of Web Project subject on UdL.

## Installation

Manual installation of the project:

1. Clone the repository

```bash
git clone https://github.com/Computer-Engineering-UdL/Game-Management.git
```

2. Navigate to the project folder

```bash
cd Game-Management
```

3. Install the required packages using [Poetry](https://python-poetry.org/)

- **Option 1**: In case you want to develop the project, you can install the development dependencies by running the following command:
    ```bash
    poetry install
    ```
    Remember to activate the virtual environment by running the following command:
    ```bash
    poetry shell
    ```

> [!NOTE]
> For more information check the [CONTRIBUTING](.github/CONTRIBUTING.md) file.


- **Option 2**: In case you want to run the project, you can install the production dependencies by running the following command:

    ```bash
    poetry install --no-dev
    ```

## Deploy

### Local deployment
1. Access the virtual environment
```bash
poetry shell
```
2. Run the application
```bash
python manage.py runserver
```
Also, you can apply the following commands to generate and apply the database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Docker deployment

1. Build and run the containers
```bash
docker-compose up
```
2. Open a new terminal, and access the desired container
```bash
docker exec -it <container_name> || <container_id> bash
```
If the app container is accessed you apply the following command to start managing the migrations and orchestrating the app:
```bash
poetry shell
```
Otherwise, if the db container is accessed, we can do database administration tasks. A good way to directly access the database is:
```bash
docker exec -it <db_container_name> || <db_container_id> psql -U admin -d app_db
```

For both, when the app is running, open your browser and go to the [localhost](http://localhost:8000/) url.

> [!IMPORTANT]
> If any dependency exception occurs it's probably because you have to run
> ```bash
> poetry lock
> ```
> ```bash
> poetry install
>  ```

## Matrix of responsibilities

In order to organize the work, we have divided the project into different sectors and assigned people to each of them.

| **Sector**         | **People involved**          |
|--------------------|------------------------------|
| Frontend           | Abel, Carles, Oriol & Júlia  |
| Backend            | Aniol, Aleix, Carles & Oriol |
| Testing            | Carles & Júlia               |
| Database           | Aniol & Aleix                |
| Project Management | Aniol                        |
| Deployment         | Aleix                        |

## Contributing

To contribute to this project go to the [CONTRIBUTING](.github/CONTRIBUTING.md) file.

## Licence

This project is under [MIT Licence](https://opensource.org/license/mit/) - see the [LICENCE](./LICENSE) file for
details.

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?)](https://opensource.org/license/mit/)

## Authors

The [Web Project team](https://github.com/orgs/Computer-Engineering-UdL/teams/project-web) is composed by:

- [Nogales López, Júlia](https://github.com/julianogales)
- [Pérez Salvia, Abel](https://github.com/Abelitux)
- [Segura Paz, Aleix](https://github.com/aleixsegura)
- [Serrano Ortega, Aniol](https://github.com/Aniol0012)
- [Soldevila Solsona, Oriol](https://github.com/Oriol-Solde)
- [Sànchez Hidalgo, Carles](https://github.com/carless7)

