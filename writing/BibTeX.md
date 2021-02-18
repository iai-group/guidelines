# BibTeX conventions

## Bib entries

  * Keep all bib entries in a separate .bib file.
  * **Keep the .bib file tidy**: it should contain **only papers that are actually referenced** in the current paper (not all your personal bibliography!) and **only with the required metadata fields**.
  * The ultimate source of BibTeX entries is the [ACM Digital Library](http://dl.acm.org/). If the paper cannot be found there, the same conventions should still be followed.

## BibTeX fields

  * **Bib keys**: `author:year:FTL`, where FTL are first three capital letters from the title. For example, `Balog:2012:ERL`, `Meij:2012:ASM`.

### Fields for conference/workshop papers

  * To include:
    - `author`
    - `title`
    - `booktitle`
    - `series` (`ACR 'YY` that is, acronym space 'year)
    - `pages` (`xx--yy` that is, double dash)
    - `year`
  * Not to include: `publisher`, `address`, `abstract`, `keywords`, `doi`, `url`, etc.
  * Example
  ```
  @inproceedings{Zhang:2020:ECR,
	  author = {Zhang, Shuo and Balog, Krisztian},
	  title = {Evaluating Conversational Recommender Systems via User Simulation},
	  booktitle = {Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining},
    series = {KDD '20},
	  pages = {1512--1520},
    year = {2020}
  }
  ```

### Fields for journal papers

  * To include:
    - `author`
    - `title`
    - `journal` using ISO 4 abbreviation
    - `volume`
    - `number`
    - `pages` (`xx--yy` that is, double dash)
    - `year`
  * Not to include: `publisher`, `address`, `abstract`, `keywords`, `doi`, `url`, etc.
  * Example
  ```
  @article{Sanderson:2010:TCB,
    author = {Sanderson, Mark},
    title = {Test Collection Based Evaluation of Information Retrieval Systems},
    journal = {Found. Trends Inf. Retr.},
    volume = {4},
    number = {4},
    pages = {247--375},
    year = {2010}
  }
  ```

### Fields for arXiv papers

  * To include:
    - `author`
    - `title`
    - `journal = {CoRR}`
    - `volume = {abs/PAPER_ID}`
    - `archivePrefix = {arXiv}`
    - `eprint = {PAPER_ID}`
    - `year`
  * Not to include: `url`
  * Example
  ```
  @article{Balog:2020:CCC,
    author = {Krisztian Balog and Lucie Flekova and Matthias Hagen and Rosie Jones and Martin Potthast and Filip Radlinski and Mark Sanderson and Svitlana Vakulenko and Hamed Zamani},
    title = {Common Conversational Community Prototype: Scholarly Conversational Assistant},
    journal = {CoRR},
    volume = {abs/2001.06910},
    archivePrefix = {arXiv},
    eprint = {2001.06910},
    year = {2020}
  }
  ```  

### Fields for books

  * To include:
    - `author`
    - `title`
    - `publisher`
    - `year`
  * Optional
    - `series`
    - `volume`
  * Not to include: `address`, `doi`, `isbn`, `url`, etc.
  * Example
  ```
  @book{Balog:2018:EOS,
    author = {Krisztian Balog},
    title = {Entity-Oriented Search},
    series = {The Information Retrieval Series},
    volume = {39},
    publisher = {Springer},
    year = {2018}
  }
  ```

### Fields for PhD theses

  * To include:
    - `author`
    - `title`
    - `school`
    - `year`
  * Not to include: `address`, `doi`, `isbn`, `url`, etc.
  * Example
  ```
  @phdthesis{Maxwell:2019:MSS,
    author = {Maxwell, David Martin},
    title = {Modelling search and stopping in interactive information retrieval},
    school = {University of Glasgow},
    year = {2019}
  }  
  ```

## Natbib

  * Always use [natbib](https://www.overleaf.com/learn/latex/natbib_citation_styles)!
  * Use `\citet{}` is for textual citation. For example, `\citet{Smith:2000:ABC} proposed ...` => `Smith et al. (2000) proposed...`
  * Use `\citep{}` for parenthetical citation. For example, `In \citet{Smith:2000:ABC} the idea of ...` => `In [2] the idea of...`
  * Never write out `Smith et al.`, there is a `\citeauthor{}` command for that (but most likely what you're looking for is actually `\citet{}`).
