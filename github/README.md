# GitHub

We use git, and more specifically GitHub, for collaborative work on papers and projects.

[Following GitHub](https://github.com/github/renaming), we use `main` as the default branch (as opposed to `master`).

## Initial setup

  * Create a GitHub repository based on the [IAI project template](https://github.com/iai-group/template-project) (click "Use this template").
  * Add your collaborators.
  * See pre-commit hook configuration down below.

## Workflow

By default, we use the [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow), where a separate branch is created for each new feature.
(Alternatively, for larger projects where periodic feature releases are planned, [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) may be used.)

  * Create an issue for the feature/writing TODO.
  * Create a feature branch off the latest state of the project, i.e., the main branch.  Name the branch using the `feature/[issue_no]-[description]` pattern, e.g., `feature/27-adding-term-weighting`:
    ```
    git checkout main
    git fetch origin
    git reset --hard origin/main
    git checkout -b feature/27-adding-term-weighting
    ```
  * Commit changes
    - Follow the [guide for commit messages](Git_commit.md).
    - Last commit should contain "Closes #issue_number".
  * (Optionally) If you need to sync up your branch to main, you can do that by issuing:
    ```
    git checkout main
    git pull
    git checkout feature/#27-adding-term-weighting
    git merge main
    ```
  * Ask for a code review
    - See [Code review best practices](https://google.github.io/eng-practices/review/).
    - Iterate with the reviewer until all open issues are addressed and you get an LGTM from all reviewers.
  * Merge changes into `main`.  


## Pre-commit hooks

See the [the section on pre-commit hooks under the Python style guide](https://github.com/iai-group/guidelines/tree/main/python#install-pre-commit-hooks).
