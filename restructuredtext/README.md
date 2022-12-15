# IAI reStructuredText Style Guide

## Naming conventions

  * Files names are lowercased and `_` -separated (e.g., `writing_style.rst`).

## Headings

  * Each file should start with a section heading block on line 1.
  * Marker characters to use (in this order): 
    1. Section: `==`
    1. Subsection: `--`
    1. Subsubsection: `^^`
    1. Paragraph: `""`
  * The heading marker character line should be the same length as the heading text.
  * There should be an empty line before and after header blocks.
    - The only exception to this rule is the heading on line 1 of a file.

```rst
This is a section
=================

This is a subsection
--------------------

This is a subsubsection
^^^^^^^^^^^^^^^^^^^^^^^

This is a paragraph
"""""""""""""""""""
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
    - Sub item 212

  - Sub item 22

* List item 3
```

<<<<<<< HEAD
## Links

### Referencing Python objects

  * Reference a module with `:py:mod:` followed by the name of the module (e.g., `` :py:mod:`package.module` ``).
  * Reference a class with `:py:class:` followed by the name of the class (e.g., `` :py:class:`package.module.class` ``).
  * Reference a function with `:py:func:` followed by the name of the function (e.g., `` :py:func:`package.module.function` ``).
  * More details [here](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cross-referencing-python-objects).

### Linking dynamically generated pages

```
:doc:`api/nordlys.core.retrieval`
```

By default the name is the title of the page.
To use a custom link:

```
:doc:`Retrieval <api/nordlys.core.retrieval>`
```

### Linking external pages

```
External hyperlinks, like `Python <http://www.python.org/>`_. Mind that you need the "_" in the end.
```


### Linking headings within the document

```
* :ref:`my_label`

[...]

.. _my_label::

My Heading 
----------

```


## Annotations

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

### Notes

```
.. note:: Your text comes here
```

### TODOs

```
.. todo:: Your text comes here
```

## Additional resources

  * [Sphinx reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
