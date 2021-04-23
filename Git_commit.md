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

It's helpful to think that the subject should complete the sentence

  * If applied, this commit will *your subject line here*

### Body

If you need more than one 50 character line to explain your change, write a body under the subject in the commit message.

The body should be
  * separated from the subject by one blank line,
  * (manually) wrapped at 72 characters, and
  * an explanation of why and what was changed, not how it works. 

### Issue tracking

Put references to repository issues at the bottom of the body, as in the example.

## Example

This example is taken directly from the [blog post](https://chris.beams.io/posts/git-commit/).

```
Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequences of this
change? Here's the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```


## What's the use?

You can look at the commit messages later, e.g. by the command `git log`. 
