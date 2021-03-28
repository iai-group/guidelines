# IAI Python Style Guide

Keep in mind that **сode is read more often than it is written**.

We follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html). This document highlights a number of peculiarities to pay special attention to, as well as complements the Google style guide on issues not specified there.

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

## Amendments to the Google Python Style Guide

  * Use single quotes `'` (as opposed to `"`) everywhere, except docstrings.

## IDE

You are strongly encouraged to use [PyCharm](https://www.jetbrains.com/pycharm/) as IDE. A [free educational license](https://www.jetbrains.com/community/education/) is available for both students and educators.  However, any other IDE may be used as long as it is configured according to the settings below.

### IDE Configuration

  * Set maximum line length to 80 characters.
  * Use spaces (instead of tabs) for indentation.
