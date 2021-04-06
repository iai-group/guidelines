# IAI Python Style Guide

Keep in mind that **сode is read more often than it is written**.

We follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html). This document highlights a number of peculiarities to pay special attention to, and potentially complements the Google style guide on issues not specified there.

*TODO(Ivica) Blurb on using virtual environments.* Unless stated otherwise, we assume Python 3.6+.

We use an auto-formatter (specifically, [Black](https://github.com/psf/black)) to ensure that we are consistent with the style guide.  This directly reduces the need for discussions about formatting questions.

*TODO(Krisztian): Paragraph on linting."

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

## Virtual environments

*TODO(Ivica)*

## Linting and code analysis using Flake8

*TODO: Linting is the automatic process of checking for programmatic and stylistic errors.*

We use [Flake8](http://flake8.pycqa.org/en/latest/), which is a great toolkit for checking against coding style (PEP8), programming errors (such as "library imported but unused" and "Undefined name") and to check cyclomatic complexity (which is a measure of the number of independent paths through the source code). Flake8 essentially wraps pep8, pyflakes, and Ned Batchelder's McCabe script.

  * Install using `pip install flake8`.
  * *TODO: See PyCharm configuration below.*


## Automatic formatting using Black

The main incentive for using Black is to avoid having to think about many configuration options. Black reformats entire files in place.

  * Install Black using `pip install black`.
  * Have the following block in the `pyproject.toml` file in the repo root:
    ```
    [tool.black]
    line-length = 80
    target-version = ['py37']
    ```
  * See PyCharm configuration below.

## PyCharm configuration (one-time)

  * Flake8
    - *TODO*
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
