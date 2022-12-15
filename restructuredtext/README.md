# IAI reStructuredText Style Guide

## Naming conventions

  * Files names are lowercased and `_` -separated (e.g., `writing_style.rst`).

## Headings

  * Each file should start with a section heading block (`=`) on line 1.
  * The heading marker character line should be the same length as the heading text.
  * There should be an empty line before and after header blocks.
    - The only exception to this rule is the heading on line 1 of a file.

```rst
This is the main title
======================

This is the subtitle
--------------------

This is the subsubtitle
""""""""""""""""""""

This is the subsubsubtitle
^^^^^^^^^^^^^^^^^^^^^^^

```

## Lists

  * Top-level lists are marked by `*`, second, third, etc. levels below are marked by `-`.
  * Non top-level items are indented by 2 spaces.
  * Nested lists items have to be separated from the top-level list items by blank lines.

```rst
* List item 1
* List item 2

  - Sub item 21

    - Sub item 211

  - Sub item 22

* List item 3
```

## Code blocks

  * Use the following directive to insert a block of code: `.. code-block:: [language]`.
  * There should be an empty line before and after the directive and after the code.

Example:
```rst
See python code block below.

.. code-block:: python

  import os

This is a new paragraph.
```

## References python objects

  * Reference a module with `:py:mod:` followed by the name of the module (e.g., `` :py:mod:`package.module` ``).
  * Reference a class with `:py:class:` followed by the name of the class (e.g., `` :py:class:`package.module.class` ``).
  * Reference a function with `:py:func:` followed by the name of the function (e.g., `` :py:func:`package.module.function` ``).
  * More details [here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cross-referencing-python-objects).

## Additional resources

  * [Sphinx reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
