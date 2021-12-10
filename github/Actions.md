# GitHub Actions

GitHub actions provide a convenient place to run validation scripts for the project, e.g., build, black, flake8, pytest.

## Setup

There should be a YAML file under `.github/workflows/` folder as part of the repository that will be executed automatically based on configuration (usually on push and/or when creating a new pull request).

See example [here](xsresources/python-package-conda.yaml).

## Components

### General

Name of the action and the trigger.
```
name: build

on: [push, pull_request]
```

# Jobs

Jobs component sets up the server and the steps that should be executed. In this example we install dependencies using conda; run tests for `black`, `flake8`, and `pytest`; and upload results to CodeCov for test coverage analysis. **NB! In order to use CodeCov API, CODECOV_TOKEN needs to be added to secrets under the repository settings**

```
jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 5

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.7
      uses: actions/setup-python@v2
      with:
        python-version: 3.7
    - name: Add conda to system path
      run: |
        # $CONDA is an environment variable pointing to the root of the miniconda directory
        echo $CONDA/bin >> $GITHUB_PATH
    - name: Install dependencies
      run: |
        conda env update --file environment.yml --name base
    - name: Check black formatting
      run: |
        black .
    - name: Lint with flake8
      run: |
        flake8 .
    - name: Run tests
      run: |
        pytest tests --cov=./ --cov-report=xml
    - name: "Upload coverage to Codecov"
      uses: codecov/codecov-action@v2
      with:
        token: ${{ secrets.CODECOV_TOKEN }}
```
