# Contribute to IAI repositories

Everyone is welcome to get involved and we appreciate everybody's contribution.
Code contributions are not the only way to be involved. 
Proposing new features or improvement, giving feedback, and improving the documentation are also valuable to improve a library.

## Ways to contribute

There are several ways you can contribute:

  * Fix open issues.
  * Submit new issues related to desired feature, new ideas, or bugs.
  * Contribute to the documentation.

## Fix open issues

If you have an idea to fix an open issue, feel free to work on it and open a [Pull Request](#create-a-pull-request).

## Submitting a new issue

Please follow these guidelines when submitting a new bug-related issue or feature request to facilitate the management. 

### Bug-related issue

Before creating a bug-related issue, please make sure it has not been reported before (use the search feature under Issues) to avoid duplicated issues.
If you are unsure whether the bug is in your code or the library, please use the label `question` so we can do our best to help and give you feedback.

After confirming that the bug is coming from the library and has not been reported before, please create an issue with the following information:

  * Include information related to your environment such as OS type and version and Python version.
  * A short description of the bug along with a code snippet to reproduce it.
  * The full traceback if an exception is raised.
  * Any additional information that you deem relevant.
  * Add the label `bug`.

### Feature request

To request a new feature, please create a new issue with the following information:

  * Why do you want this feature? Is it for a specific project? Is it something that the library is lacking? Is it an added value to the library?  
  * Give a detailed description of the new feature.
  * If possible, provide a code snippet illustrating the usage.

A well written issue will facilitate the integration of the requested feature. 

## Contribute to the documentation

We are constantly looking for ways to make the documentation clearer and more accurate.
Please let us know how the documentation can be improved such as typos and any content that is missing, unclear or inaccurate. 
We will be happy to review your suggestion or to make changes!

## Create a Pull Request

We strongly suggest you to check the existing PRs or issues before developing any code to make sure no one else is working on the same issue already.
If you are unsure, it is a good idea to comment on the related issue to check if someone is already on it. 

Basic proficiency with `git` is necessary to contribute to the library and the code requires Python 3.9.
Follow the steps below to start contributing:

  * Fork the repository with the **Fork** button on the repository page.
  * Clone your fork locally, and add the base repository as remote:

  ```shell
  git clone <URL to your fork>
  cd <local fork directory>
  git remote add upstream <URL of original repository>
  ``` 
  
  * Create a new branch to commit your development changes. **Do not work on the main branch**.

  ```shell
  git checkout -b descriptive-branch-name
  ```

  * Create a development environment as detailed [here](https://github.com/iai-group/guidelines/blob/main/python/README.md#local-development-configuration).
  * Develop on your branch.  

    - As you work on the code, you can run the tests under `tests` with `pytest tests -vv`. For new feature, we would appreciate if you could develop the related tests and improve the robustness of the library.  
    - If you work on the documentation, you can build it locally with this command: `sphinx-multiversion docs/source build/html`. Please make sure that the required packages are installed before running the command. This command will create the documentation locally under `build/html`.
  
  * Once the development is finished:
  
    - The modified files can be added with `git add` and commited with `git commit`. Please remember to write a [good commit message](Git_commit.md).
    - To keep your copy of the code up to date with the original repository, rebase your branch on upstream/branch before you open a pull request:

    ```shell
    git fetch upstream
    git rebase upstream/main
    ```

    - Push you changes: `git push -u origin descriptive-branch-name`. If a PR is already open use the `--force` flag.

  * To open a PR, go to your forked repository on GitHub and click on **Pull Request**. Please make sure to describe what the PR changes and mention the related issue in the PR description. More information on the code review [here](Code_review.md).


## Conventions

We follow the [IAI Python Style Guide](https://github.com/iai-group/styleguide/tree/main/python).