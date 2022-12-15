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

## Links

### Link a dynamically generated page

```
:doc:`api/nordlys.core.retrieval`
```

By default the name is the title of the page.
To use a custom link:

```
:doc:`Retrieval <api/nordlys.core.retrieval>`
```

### Link to an external page

```
External hyperlinks, like `Python <http://www.python.org/>`_. Mind that you need the "_" in the end.
```


### Link to a heading within a document

```
* :ref:`my_label`

[...]

.. _my_label::

My Heading 
----------

```

### Link to a module or package

```
:py:mod:`nordlys.services.el`
```

For referencing other Python objects, see http://www.sphinx-doc.org/en/stable/domains.html#python-roles


## Annotations

### Notes

```
.. note:: Your text comes here
```

### TODOs

```
.. todo:: Your text comes here
```

### Code blocks

```
.. code:: python
```

## Additional resources

  * [Sphinx reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
