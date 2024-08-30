# Contributing to FastAPI-Endpoints

I am very eager to see what you can contribute to **FastAPI-Endpoints**! All contributors are welcomed here. Below is a guide to help you get started.

## How to Contribute

### Reporting Bugs

If you've found a bug, please open an issue and provide as much detail as possible:

- A clear and descriptive title.
- Steps to reproduce the bug.
- Expected and actual behavior.
- Any error messages or logs.
- Add the `bug` tag.
- Assign the issue to a maintainer.

### Suggesting Features

We appreciate feature suggestions! Please open an issue with the following:

- A clear and descriptive title.
- A detailed explanation of the feature.
- Potential use cases or examples.
- Any relevant screenshots or mockups.
- Add the `feature-request` tag.
- Assign the issue to a maintainer.

### Submitting Code Changes

If you want to contribute code:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-new-feature`). It is very important to use the `feature/` prefix to the branch.
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/my-new-feature`).
5. Open a pull request and provide details about What, Why, How things got changed.

## Development Setup

Here’s how to set up the project on your local machine. The project is heavily using [Poetry](https://python-poetry.org/) so its expected to have that installed.
Create a new environment using either [venv](https://docs.python.org/3/library/venv.html) or [pyenv](https://github.com/pyenv/pyenv) for all the supported python versions of `fastapi-endpoints`.

1. Clone the repository: `git clone https://github.com/yourusername/yourprojectname.git`
2. Navigate to the project directory: `cd yourprojectname`
3. Install dependencies: `poetry install`
4. Make changes to the project.
5. Check formatting using `ruff format --check` if there are any issues resolve them with `ruff format`
6. Check lint using `ruff check` if there are any issues resolve them in the code.
7. Run the tests `pytest`

## Style Guide

- **Imports**:
  - Place all imports at the top of the file, just after any module comments and docstrings.
  - Use absolute imports whenever possible.
  - Group imports into three sections, in this order: standard library imports, third-party imports, and local application/library-specific imports. Each group should be separated by a blank line.
  - Example:
    ```python
    import os
    import sys

    import requests

    from my_project import my_module
    ```
- **Docstrings**:
  - Use docstrings to describe modules, classes, and functions.
  - Follow the [PEP 257](https://www.python.org/dev/peps/pep-0257/) conventions for docstrings.

- **Type Annotations**:
  - Use type annotations to specify the expected data types of function arguments and return values.
  - Example:
    ```python
    def add(a: int, b: int) -> int:
        return a + b
    ```

## Commit Messages

Use meaningful commit messages to describe the changes you have made. Follow this format:

