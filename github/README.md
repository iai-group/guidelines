# GitHub

We use git, and more specifically GitHub, for collaborative work on papers and projects.

## Papers

### Initial setup

  * Create a GitHub repository based on the [IAI paper template](https://github.com/iai-group/template-paper) (click "Use this template").
  * Name your repository following the `[conf][year]-[short_title]` pattern, where
    - `conf` is the conference acronym lowercased,
    - `year` is the year (4 digits),
    - `short_title` is a 3-10 character long title.
    - For example: `kdd2020-usersim` or `emnlp2021-kgqa`.
  * Add your collaborators.

### Workflow

For papers, we follow the [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow), where a separate branch is created for each new feature.

  * Create an issue for the feature/writing TODO.
  * Create a feature branch off the latest state of the project, i.e., the master branch.  Name the branch using the `feature/#[issue_no]-[description]` pattern, e.g., `#27-adding-term-weighting`:
    ```
    git checkout master
    git fetch origin
    git reset --hard origin/master
    git checkout -b feature/#27-adding-term-weighting
    ```
  * Commit changes; last commit should contain "closing #issue_number".
  * Ask for a code review
    - See [Code review best practices](https://google.github.io/eng-practices/review/).
    - Iterate with the reviewer until all open issues are addressed and you get an LGTM from all reviewers.
  * Merge changes into `master`.


### Post acceptance

Release the resources using the [IAI paper release template](https://github.com/iai-group/template-paper-release).

## Projects

For projects, one may choose between the [Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) and [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).  The latter makes sense for larger projects where periodic feature releases are planned.
