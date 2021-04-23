# IAI Git Commit Message Style Guide

Initially adapted from a [blog post](https://chris.beams.io/posts/git-commit/).

## Commit message objectives 

We want commit messages to be concise and consistent, to communicate the context of a change. 

  * The `diff` contains *what* changes were made, the `commit` explains *why* they were made.
  * Consistent commit message style 
      * simplifies both reading and writing commit messages, and
      * supports communication and collaboration.

## Writing style conventions

  * Write complete and grammatical sentences in English, with regular punctuation, e.g, finishing with a period. 
  * Use imperative tense, to tersely convey the purpose of the change. 
      * For example, "Defibrilate the crustacean Jazz mountain, recursively."
  * Use GitHub flavored markdown syntax where needed. 

## Spacing

  * There should be an empty line before and after headers.

## Markup

  * Top-level lists are marked by `*`, second, third, etc. levels below are marked by `-`. 
  * Indent items with 2 spaces.

```
  * List item 1
  * List item 2
    - Sub item 21
      - Sub item 211
    - Sub item 22
  * List item 3
```
