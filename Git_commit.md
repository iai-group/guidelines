# IAI Git Commit Message Style Guide

Initially adapted from a [blog post](https://chris.beams.io/posts/git-commit/).

## Commit message objectives 

We want commit messages to be concise and consistent, to communicate the context of a change. 

  * The `diff` contains *what* and *how* changes were made, the `commit` primarily explains *why* they were made.
  * Consistent commit message style 
      * simplifies both reading and writing commit messages, and
      * supports communication and collaboration.

## Context

There are different ways and contexts whereby a commit message is added, but for simplicity we assume you made some changes, and did the following commands in the terminal:
```
git add .
git commit
```

You will then have vi open and provide the following starting point:
```

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch master
# Your branch is up to date with 'origin/master'.
#
# Changes to be committed:
#       new file:   foo
#
```

And then your job is to write a good commit message! Document why you are making the commit and the associated changes.

## Rules

You should at least write a single line if your commit only needs a brief explanation. We'll call this the subject, whether or not you also write a longer text, called the body, below the subject. 

### Subject

The subject should be
  * captialized, e.g. *Combine the Christmas lighbulbs*,
  * maximum 50 characters,
  * written with no terminating period, and
  * the subject should be written in the *imperative mood*.

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
