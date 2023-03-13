# Hosting a versioned documentation on GitHub Pages

This page describes how to create versioned documentation and host it on a GitHub page.

The versioned documentation is built with [sphinx-multiversion](https://holzhaus.github.io/sphinx-multiversion/master/index.html).

## Requirements

The following requirements need to be installed:

```txt
sphinx<5.0;
scipy==1.7.2;
sphinx;
sphinx_rtd_theme;
sphinxcontrib-bibtex;
nbsphinx;
recommonmark;
sphinx-markdown-tables;
sphinx-autoapi
myst-parser
sphinx-multiversion==0.2.4
```

It is recommended to add them to `requirements.txt`, so they can easily be installed and maintained.

## Documentation recommended organization

To be able to use the [workflow](#workflow) below, the documentation needs to be organized as follows: 

```
.
├── docs
│   ├── README.md
│   ├── source
│   │   ├── _static                     # Contains documentation images 
│   │   │   └── image.png               
│   │   ├── _templates
│   │   │   └── versions.html           # HTML to display the different versions
│   │   ├── conf.py                     # Documentation configuration
│   │   ├── installation.rst            # Documentation files
│   │   └── index.rst                   # Documentation index
```

The documentation is written in `.rst` files and the configuration is defined in `conf.py`.

## Build the documentation locally

To build the documentation locally use the following command:

```bash
sphinx-multiversion docs/source build/html
```

This will create the documentation for each version of the package under the folder `build/html`. Each version has its own folder.

## Workflow

A GitHub workflow and action can be used to automatically build and host an up-to-date documentation when the `main` branch is updated.

  * Create new workflow `build_docs.yaml`

```yaml
name: Sphinx docs to gh-pages

on:
  push:
    branches:
      - main

jobs:
  sphinx_docs_to_gh-pages:
    runs-on: ubuntu-latest
    name: Sphinx docs to gh-pages
    steps:
      - name: Checkout branch
        uses: actions/checkout@v3
        with:
          ref: main
          fetch-depth: 0
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.9.15
          cache: "pip"
      - name: Installing the Documentation requirements
        run: |
          pip3 install -r requirements.txt
      - name: Sphinx docs to GitHub Pages
        uses: ./.github/actions/build_docs/
        with:
          branch: main
          dir_docs: docs/source
          sphinxapiopts: '--separate -o . ../'
          sphinxapiexclude: '../*setup* ../*.ipynb'
          sphinxopts: ''
```

  * Create a new action `action.yaml` under `.github/workflow/actions/build_docs`. This action builds a versioned documentation based the configuration.

```yaml
name: 'Sphinx docs to GitHub Pages'
description: 'Automatic Sphinx html docs compilation and deployment through the gh-pages branch.'
author: "Diego Prada-Gracia"
branding:
  icon: "upload-cloud"
  color: "orange"
inputs:
  branch:
    description: Name of the branch where the sphinx documentation is located
    required: false
    default: 'main'
  dir_docs:
    description: Path where the sphinx documentation is located
    required: false
    default: 'docs'
  sphinxapiexclude:
    description: Files/directories to exclude from sphinx-apidoc
    require: false
    default: '*setup* tests*'
  sphinxapiopts:
    description: Options for sphinx-apidoc (default outputs to dir_docs and searches for modules one level up)
    require: false
    default: '-o . ../'
  sphinxopts:
    description: Compilation options for sphinx-multiversion
    required: false
    default: ''

runs:
  using: "composite"
  steps:
    - name: setting the committer name and email
      id: committer
      shell: bash
      run: |
        author_name="$(git show --format=%an -s)"
        author_email="$(git show --format=%ae -s)"
        echo "::group::Set committer"
        echo "git config user.name $author_name"
        git config user.name $author_name
        echo "git config user.email $author_email"
        git config user.email $author_email
        echo "::endgroup::"
    - name: gh-pages branch creation if needed
      id: gh-pages-branch-creation
      shell: bash
      run: |
        echo "::group::Checking if gh-pages branch exists"
        if [[ -z $(git ls-remote --heads origin gh-pages) ]]; then
           echo "Creating gh-pages branch"
           git checkout --orphan gh-pages
           git reset --hard
           git commit --allow-empty -m "First commit to create gh-pages branch"
           git push origin gh-pages
           echo "Created gh-pages branch"
        else
           echo "Branch gh-pages already exists"
        fi
        echo "::endgroup::"
    - name: Moving to branch where sphinx docs are located
      id: to-branch-with-docs
      shell: bash
      run: |
           git checkout ${{ inputs.branch }}
    - name: sphinx apidoc generation
      shell: bash -l {0}
      working-directory: ./${{ inputs.dir_docs }}
      run: |
        echo ::group::Sphinx apidocs generation
        sphinx-apidoc ${{ inputs.sphinxapiopts }}  ${{ inputs.sphinxapiexclude }}
        echo ::endgroup::
    - name: sphinx html docs compilation
      shell: bash -l {0}      # This is needed to work with conda here. See:https://github.com/marketplace/actions/setup-miniconda#IMPORTANT
      working-directory: ./${{ inputs.dir_docs }}
      run: |
        echo ::group::Sphinx docs compilation
        sphinx-multiversion . _build ${{ inputs.sphinxopts }}
        echo ::endgroup::
    - name: pushing to gh-pages
      shell: bash
      run: |
        echo ::group::Create README for gh-pages
        SHA=$GITHUB_SHA
        echo "$SHA $GITHUB_EVENT_NAME"
        if [ "$GITHUB_EVENT_NAME" == "pull_request" ]; then
            SHA=$(cat $GITHUB_EVENT_PATH | jq -r .pull_request.head.sha)
        fi
        SHORT_SHA="$(git rev-parse --short $SHA)"
        DIR_HTML=${{ inputs.dir_docs }}/_build/
        echo "#GitHub Pages" > $DIR_HTML/README.md
        echo "" >> $DIR_HTML/README.md
        echo "Last update of sphinx html documentation from [$SHORT_SHA](https://github.com/$GITHUB_REPOSITORY/tree/$SHA)" >> $DIR_HTML/README.md
        cat $DIR_HTML/README.md
        echo ::endgroup::
        echo ::group::Create .nojekyll in case 'sphinx.ext.githubpages' is not used
        touch $DIR_HTML/.nojekyll
        echo ::endgroup::
        echo ::group::Push to gh-pages
        git add -f $DIR_HTML
        git commit -m "From $GITHUB_REF $SHA"
        git push origin `git subtree split --prefix $DIR_HTML ${{ inputs.branch }}`:gh-pages --force
        echo ::endgroup::
```

This workflow will create/update the branch `gh-pages` with a folder for each version of the documentation.