# IAI Python Style Guide

Keep in mind that **сode is read more often than it is written**.

We follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).  This document highlights a number of peculiarities to pay special attention to, and potentially complements the Google style guide on issues not specified there.

**Unless stated otherwise, we assume Python 3.9.**

Linting is the automatic process of checking for programmatic and stylistic errors.  We use [Flake8](http://flake8.pycqa.org/en/latest/), which is a great toolkit for checking against coding style (PEP8), programming errors (such as "library imported but unused" and "Undefined name") and to check cyclomatic complexity (which is a measure of the number of independent paths through the source code).  Flake8 essentially wraps pep8, pyflakes, and Ned Batchelder's McCabe script.  

Additionally, we use Mypy. It is a static type checker for Python that aims to combine the benefits of dynamic and static typing. Mypy type checks programs that have type annotations conforming to PEP 484.

We also use an auto-formatter to ensure that we are consistent with the style guide.  This directly reduces the need for discussions about formatting questions.  In particular, we use [Black](https://github.com/psf/black).  The main incentive for using Black is to avoid having to think about many configuration options.  Black reformats entire files in place.

In addition to code, we also use auto-formatter for docstrings called [docformatter](https://pypi.org/project/docformatter/). It ensures all docstrings conform to the Google docstring style we follow.

You are strongly encouraged to use [VSCode](https://code.visualstudio.com/) as IDE. This is a free, highly customisable text editor. We provide detailed instructions on the customisations we use [here](vscode/).  However, any other IDE may be used as long as it is configured accordingly.

## Highlighted from the Google Python Style Guide

  * Maximum line length is 80 characters.
  * Indent code blocks with 4 spaces.
  * Use parentheses sparingly.
  * Naming: `module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`, `function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`, `function_parameter_name`, `local_var_name`
    - Avoid dashes (`-`) in any package/module name.
    - Use single underscore for private/protected methods/variables (avoid "dunder"-s).
  * [Google-style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings):
    - Summary line, blank line, followed by the rest of the docstring.
    - All sentences must be terminated by a period, question mark, or exclamation point.
    - The docstring should be descriptive-style ("Fetches rows from a Bigtable.") rather than imperative-style ("Fetch rows from a Bigtable.").
    - Use `Args:`, `Returns:`, and `Raises:` for documenting functions.
    - In case of the arguments with a description longer than one line in `Args:`, indent the following lines with 2 spaces.
  * Comments:
    - Either before the operation or on the same line.
      - Comments on the same line should start at least 2 spaces away from the code with the comment character #, followed by at least one space before the text of the comment itself.
    - Comments should be as readable as narrative text, with proper capitalization and punctuation.
  * Imports:
    - Always at the top of the file, just after any module comments and docstrings and before module globals and constants.
    - Use `from <module> import <name>` for importing a single object or `import <module>` for importing a module.
      - Do not use `from <module> import *`.
    - Imports should be grouped from most generic to least generic:
      - Standard library imports.
      - Related third party imports.
      - Local application/library specific imports.
      - A blank line between each group of imports.
      - Within each grouping, imports should be sorted lexicographically, ignoring case, according to each module's full package path.
    - Avoid relative imports and use the full package name.
      - The only exception is when importing inside `__init__.py` files. In this case, we use relative imports from the same module. This simplifies the long paths when importing to other modules.

## Amendments to the Google style guide

  * Docstrings
    - The class constructor should be documented in the docstring for its `__init__` method.  The class docstring is omitted.
  * Always use double quotes `"` (but if you have Black configured, it should enforce those automatically)
  * Use [f-strings](https://www.python.org/dev/peps/pep-0498/) for string formatting

## Repository set-up

The following steps are to be performed when setting up a new code repository.

*TODO: Create an example repository that is already configured this way.*

### Requirements

Create a `requirements.txt` file which includes the following packages:

```
black
flake8
pytest
mypy
docformatter
pre-commit
```

### Flake8

  * Create a `.flake8` file in the repo root with the following default settings:

     ```.flake8
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

    ```toml
    [tool.black]
    line-length = 80
    target-version = ['py37']
    ```

  * Include the Black badge in the repo README.md:

    ```markdown
    [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
    ```

### Pytest

  * Create a blank `conftest.py` file.
  * Create a folder called `tests` at the root of the repository and make it a module by creating a `__init__.py` file.
  * Use the same module structure under `tests` as the source code, with files prefixed with `test_`.
  * If you need to run the tests explicitly without needing to commit run `pytest tests -vv` use `-vv` to make it verbose.

### Install pre-commit hooks

  * This is to be done once all the requirements are (`black`, `flake8`,  `mypy`, `docformatter`, and `pre-commit`) are installed!
  * Create a `.pre-commit-config.yaml` following [this](https://github.com/iai-group/template-project/blob/main/.pre-commit-config.yaml) example.
  * Execute `pre-commit install` to install pre-commit hooks (which are defined in `.pre-commit-config.yaml`).
  * If the pytest when running as pre-commit hook fails even though all tests pass make sure there are no modified files left unstaged.
  * If Black fails with reformatted files and adding reformatted files to staging area still doesn't fix it, then run the `black file_name.py` explicitly and then add that file so the staging area and commit again.

## Local development configuration

### Virtual environments with anaconda

  * Simplest way to start using virtual environments in anaconda is with command `conda create --name myenv` where `myenv` is the name of the environment we want to create.

  * After creating the environment, we can activate it with `conda activate myenv` and deactivate with `conda deactivate`.

  * If we already know some of the libraries we want to include, we can simply append those to the end:

    ```shell
    conda create -n myenv python=3.9 pip black flake8 pre-commit pytest mypy docformatter
    ```

  * To add more libraries after we already created and activated the environment:

    ```shell
    conda install jupyter -y
    ```

    - The flag `-y` automatically answers `y` to the `Proceed ([y]/n)?` prompt.

  * Alternative 1
    * Create conda environment containing only python and pip and activate it

    ```shell
    conda create -n myenv python=3.9 pip@
    conda activate myenv
    ```

    * Install all other dependencies using pip

    ```shell
    python -m pip install -r requirements.txt
    ```

    Example file structure:

    ```txt
    black
    flake8
    mypy
    docformatter
    pre-commit
    ```

  * Alternative 2
    * create a new environment from a `.yaml` file. This file is similar to `requirements.txt` but allows for more options to be specified.

      ```shell
      conda env create -n myenv --file environment.yaml
      ```

      Example file structure:

      ```yaml
      name: <env name>
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

  * To export all dependencies to a cross platform `environment.yaml` file:

    ```shell
    conda env export --from-history > environment.yaml
    ```

    - Here, `--from-history` only includes dependencies specified by the user, omitting this will include all present dependencies. Note that you might want to remove `name` and `prefix` from the created file.
    - Using `--no-builds` will remove specific version numbers.

  * To remove an environment first deactivate and then:

    ```shell
    conda env remove -n myenv
    ```

  * More information about [Anaconda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Packages

Make sure the packages `black`, `flake8`, `pre-commit`, and `pytest` are installed.
Normally, these should be in the repository's requirements.txt file and can be installed using `pip install -r requirements.txt`.
