# Contributing

In order to contribute to this project, follow the next steps:

### 1. Conventional Commits

To maintain a clean and organized code, this project uses
the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. This means that every commit
message should follow the next pattern:

```
<type>[optional scope]: <description>
```

Where `<type>` can be one of the following:

- `chore`: Changes to the build process or auxiliary tools and libraries such as documentation generation.
- `ci`: Changes to our CI configuration files and scripts.
- `docs`: Changes to the documentation.
- `feat`: A new feature for the user, not a new feature for build script.
- `fix`: A bug fix for the user, not a fix to a build script.
- `perf`: A code change that improves performance.
- `refactor`: A code change that neither fixes a bug nor adds a feature.
- `revert`: Changes that revert a previous commit.
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semicolons, etc.).
- `test`: Adding missing tests or correcting existing tests.
- `security`: Changes that affect the security of the project.
- `translation`: Changes that affect the translation of the project.
- `changeset`: Changeset commit.
- `init`: Initial commit.
- `other`: Any other type of change.

### 2. Pull requests

Every pull request should pass its checks in order to be merged. To merge a pull request, it is necessary to be reviewed
by at least one maintainer. The pull request should also pass the following checks:

- **Ruff**: Every pull request should pass the Ruff checks in order to be merged. In order to check the code style, run the
  following command:
  ```bash
  ruff format
  ```
  To ignore any file or directory use the `--exclude` flag, for example:
  ```bash
  ruff format --exclude=venv,migrations,__pycache__,.git,docs,build,dist
  ```
  Take in mind that ruff also accept the check command to check the code style without formatting it.
  ```bash
    ruff check
    ```
- **Prettier**: Every pull request should pass the Prettier checks in order to be merged. In order to check the code style,
  run the following command:
  ```bash
  prettier --check .
  ```
  Or if you want to format the code:
  ```bash
  prettier --write .
  ```
- **Tests**: Every pull request should pass the tests in order to be merged. In order to run the tests, run the following
  command:
  ```bash
  python manage.py test
  ```
> [!NOTE]
> These commands should be run in the root directory of the project.

It is strongly recommended to create a pull request using
the [Conventional Comments](https://conventionalcomments.org/) specification.
