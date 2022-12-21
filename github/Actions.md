# GitHub Actions

GitHub actions provide a convenient place to run validation scripts for the project, e.g., build, black, flake8, pytest.

## Setup

There should be a YAML file under `.github/workflows/` folder as part of the repository that will be executed automatically based on configuration (usually on push and/or when creating a new pull request).

## Components

### General

Name of the action and the trigger.
```
name: build

on: [push, pull_request]
```

# Jobs

The jobs component sets up the server and the steps that should be executed. In [this](https://github.com/iai-group/template-project/blob/main/.github/workflows/python-package-conda.yaml) example we install dependencies; run tests for `black`, `flake8`, `mypy`, `docformatter` and `pytest`;