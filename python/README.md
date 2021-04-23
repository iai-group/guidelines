# IAI Python Style Guide

Keep in mind that **сode is read more often than it is written**.

We follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).  This document highlights a number of peculiarities to pay special attention to, and potentially complements the Google style guide on issues not specified there.

**Unless stated otherwise, we assume Python 3.7.**

Linting is the automatic process of checking for programmatic and stylistic errors.  We use [Flake8](http://flake8.pycqa.org/en/latest/), which is a great toolkit for checking against coding style (PEP8), programming errors (such as "library imported but unused" and "Undefined name") and to check cyclomatic complexity (which is a measure of the number of independent paths through the source code).  Flake8 essentially wraps pep8, pyflakes, and Ned Batchelder's McCabe script.

We also use an auto-formatter to ensure that we are consistent with the style guide.  This directly reduces the need for discussions about formatting questions.  In particular, we use [Black](https://github.com/psf/black).  The main incentive for using Black is to avoid having to think about many configuration options.  Black reformats entire files in place.

You are strongly encouraged to use [PyCharm](https://www.jetbrains.com/pycharm/) as IDE. A [free educational license](https://www.jetbrains.com/community/education/) is available for both students and educators.  However, any other IDE may be used as long as it is configured accordingly.


## Highlighted from the Google Python Style Guide

  * Maximum line length is 80 characters.
  * Indent code blocks with 4 spaces.
  * Use parentheses sparingly.
  * Naming: `module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`, `function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`, `function_parameter_name`, `local_var_name`
    - Avoid dashes (`-`) in any package/module name.
  * [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings):
    - Summary line, blank line, followed by the rest of the docstring.
    - All sentences must be terminated by a period, question mark, or exclamation point.
    - The docstring should be descriptive-style ("Fetches rows from a Bigtable.") rather than imperative-style ("Fetch rows from a Bigtable.").
    - Use `Args:`, `Returns:`, and `Raises:` for documenting functions.
  * Comments:
    - Either before the operation or on the same line.
      - Comments on the same line should start at least 2 spaces away from the code with the comment character #, followed by at least one space before the text of the comment itself.
    - Comments should be as readable as narrative text, with proper capitalization and punctuation.
  * Imports:
    - Always at the top of the file, just after any module comments and docstrings and before module globals and constants.
    - Imports should be grouped from most generic to least generic:
      - Standard library imports.
      - Related third party imports.
      - Local application/library specific imports.
      - A blank line between each group of imports.
      - Within each grouping, imports should be sorted lexicographically, ignoring case, according to each module's full package path.
    - Avoid relative imports, always use the full package name.

## Amendments to the Google style guide

  * Always use double quotes `"` (because of Black)
  * Use [f-strings](https://www.python.org/dev/peps/pep-0498/) for string formatting

## Repository set-up

The following steps are to be performed when setting up a new code repository.

*TODO: Create an example repository that is already configured this way.*

### Requirements

Create a `requirements.txt` file which includes the following packages:
```
black
flake8
pre-commit
pytest
```

### Flake8

   * Create a `.flake8` file in the repo root with the following default settings:
     ```
     [flake8]
     max-line-length = 80
     max-complexity = 10
     ignore = E203, W503
     exclude =
         .git,
         __pycache__
     ```
   * Note that some warnings need to be ignored because of conflicting formatting by Black.

### Black

  * Have the following block in the `pyproject.toml` file in the repo root:
    ```
    [tool.black]
    line-length = 80
    target-version = ['py37']
    ```
  * Include the Black badge in the repo README.md:
    ```
    [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
    ```

### Pytest

  * Create a blank `conftest.py` file.
  * Create a folder called `tests` at the root of the repository and make it a module by creating a `__init__.py` file.
  * Use the same module structure under `tests` as the source code, with files prefixed with `test_`.
  * If you need to run the tests explicitly without needing to commit run `pytest tests -vv` use `-vv` to make it verbose.

### Install pre-commit hooks

  * This is to be done once all the requirements are (black, flake8, and pre-commit) are installed!
  * Create a `.pre-commit-config.yaml` with the followings:
    ```
    repos:
    -   repo: https://github.com/ambv/black
        rev: 20.8b1
        hooks:
        - id: black
          language_version: python3.7
    -   repo: https://gitlab.com/pycqa/flake8
        rev: 3.9.0
        hooks:
        - id: flake8
    -   repo: local
        hooks:
        -   id: pytest
            name: run tests
            entry: pytest tests -vv
            language: system
            always_run: true
            pass_filenames: false
    ```
  * Execute `pre-commit install` to install pre-commit hooks (which are defined in `.pre-commit-config.yaml`).
  * If the pytest when running as pre-commit hook fails even though all tests pass make sure there are no modified files left unstaged.
  * If Black fails with reformatted files and adding reformatted files to staging area still doesn't fix it, then run the `black file_name.py` explicitly and then add that file so the staging area and commit again.


## Local development configuration

### Virtual environments with anaconda

 - Simplest way to start using virtual environments in anaconda is with command `conda create --name myenv` where `myenv` is the name of the environment we want to create.

 - After creating the environment, we can activate it with `conda activate myenv` and deactivate with `conda deactivate`.


 - If we already know some of the libraries we want to include, we can simply append those to the end:
```
conda create -n myenv python=3.7 pip black flake8 pre-commit pytest
```
To add more libraries after we already created the environment:
```
conda install jupyter -y
```
The flag `-y` automatically answers `y` to the `Proceed ([y]/n)?` prompt.

 - Alternatively, we can create a new environment from a `.yaml` file. This file is similar to `requirements.txt` but allows for more options to be specified.
```
conda env create -n myenv --file environment.yaml
```

Example file structure:
```
channels:
  - PyPi
  - conda-forge
  - defaults
dependencies:
  - python
  - pip
  - pre-commit
  - flake8
  - pytest
  - black
```

 - To export all dependencies to a cross platform `environment.yaml` file:
```
conda env export --from-history > environment.yaml
```
Here, `--from-history` only includes dependencies specified by the user, omitting this will include all present dependencies. Note that you might want to remove `name` and `prefix` from the created file.

 - To remove an environment first deactivate and then:
```
conda env remove -n myenv
```

 - More information about [anaconda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Packages

Make sure the packages `black`, `flake8`, `pre-commit`, and `pytest` are installed.
Normally, these should be in the repository's requirements.txt file and can be installed using `pip install -r requirements.txt`.

### PyCharm configuration (one-time)

  * Flake8
    - Preferences / External tools / Add (+)
    - Program: path to black (e.g., `/opt/anaconda3/bin/flake8`)
    - Arguments: `$FilePath$`
    - Working directory: `$ProjectFileDir$`
    - Setting up Flake8 issue highlighting is explained in a [separate document](PyCharm_Flake8.md)
  * Black
    - Add as an external tool
      - Preferences / External tools / Add (+)
      - Program: path to black (e.g., `/opt/anaconda3/bin/black`)
      - Arguments: `$FilePath`
      - Working directory: `$ProjectFileDir`
    - Overwrite PyCharm's default Reformat Code shortcut with Black
      - Preferences / Keymap
      - Remove "&#8997; &#8984; L" from "Reformat Code"
      - Add "&#8997; &#8984; L" to "External tools/Black"
