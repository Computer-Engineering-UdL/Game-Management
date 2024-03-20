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

<!-- > [!NOTE] -->
<!-- > For more information check the [CONTRIBUTING.md](.github/CONTRIBUTING.md) file. -->


- **Option 2**: In case you want to run the project, you can install the production dependencies by running the following command:

    ```bash
    poetry install --no-dev
    ```

## Usage

Execute the following command to start the server

```bash
python manage.py runserver
```

Then, open your browser and go to the [localhost](http://localhost:8000/) url.

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

<!--## Contributing -->

<!--To contribute to this project go to the [CONTRIBUTING.md](.github/CONTRIBUTING.md) file.-->

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

