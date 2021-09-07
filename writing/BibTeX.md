# BibTeX conventions

## Bib entries

  * Keep all bib entries in a separate .bib file.
  * **Keep the .bib file tidy**: 
    - It should contain **only papers that are actually referenced** in the current paper (not all your personal bibliography)!
    - Entries should have **only the required metadata fields**.
    - Entries should be **ordered by Bib key**.
  * The ultimate source of BibTeX entries is the [ACM Digital Library](http://dl.acm.org/). If the paper cannot be found there, the same conventions should still be followed.

## BibTeX fields

### Bib keys

Bib keys must follow the `Author:year:VENUE` format, where

  * `Author` is the name of the first author (capitalized and with accents removed).
  * In case the same first author has multiple publications in the given year at the same venue, they should be distinguished by adding an `a`, `b`, `c`, ... suffix to the year. E.g., `Smith:2010a:SIGIR`, `Smith:2010b:SIGIR`.
  * Possible values for venue may be (with this exact capitalization):
    - Conference paper: acronym (`AAAI`, `ACL`, `CIKM`, `ECIR`, `EMNLP`, `ICTIR`, `KDD`, `NeurIPS`, `SIGIR`, `TREC`, `WSDM`, `WWW`, etc.)
    - Workshop paper: workshop acronym if a well-established series (`LDOW`) or corresponding conference acronym suffixed by `-ws` (`WWW-ws`); both options are acceptable and are left to the author's best judgment (and also to check whether a more suitable reference --e.g., conference or journal follow-up paper-- may be found).
    - Journal article: acronym (`CS`, `FnTIR`, `IR`, `IRJ`, `TIST`, `TOIS`, `SIGIRForum`, etc.)
    - arXiv paper: `arXiv`
    - Book: `Book`
    - PhD thesis: `PhDThesis`

The naming of paper files should follow the same naming conventions, except that all fields are lowercased and dash is used as separator, i.e., `author-year-venue.pdf`, e.g., `smith-2020-sigir.pdf`.

### Citing conference/workshop papers

  * Fields to include:
    - `author`
    - `title`
    - `booktitle`
    - `series` (`ACR 'YY` that is, acronym space 'year)
    - `pages` (`xx--yy` that is, double dash)
    - `year`
  * Not to include: `publisher`, `address`, `abstract`, `keywords`, `doi`, `url`, etc.
  * Example
  ```
  @inproceedings{Zhang:2020:KDD,
    author = {Zhang, Shuo and Balog, Krisztian},
    title = {Evaluating Conversational Recommender Systems via User Simulation},
    booktitle = {Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining},
    series = {KDD '20},
    pages = {1512--1520},
    year = {2020}
  }
  ```

### Citing journal papers

  * Fields to include:
    - `author`
    - `title`
    - `journal` using [ISO 4 abbreviation](https://www.issn.org/services/online-services/access-to-the-ltwa/) wherever available
    - `volume`
    - `number`
    - `pages` (`xx--yy` that is, double dash)
    - `year`
  * Not to include: `publisher`, `address`, `abstract`, `keywords`, `doi`, `url`, etc.
  * Example
  ```
  @article{Sanderson:2010:FnTIR,
    author = {Sanderson, Mark},
    title = {Test Collection Based Evaluation of Information Retrieval Systems},
    journal = {Found. Trends Inf. Retr.},
    volume = {4},
    number = {4},
    pages = {247--375},
    year = {2010}
  }
  ```

### Citing arXiv papers

Depending on the paper style, arXiv papers may need different type and metadata fields.

#### Preferred format (works for ACM)

  * Paper type is `misc`!
  * Fields to include:
    - `author`
    - `title`
    - `archivePrefix = {arXiv}`
    - `eprint = {PAPER_ID}`
    - `primaryClass = {cs.CL}`
    - `year`
  * Not to include: `journal`, `url`, `volume`
  * Example
  ```
  @misc{Balog:2020:arXiv,
    author = {Krisztian Balog and Lucie Flekova and Matthias Hagen and Rosie Jones and Martin Potthast and Filip Radlinski and Mark Sanderson and Svitlana Vakulenko and Hamed Zamani},
    title = {Common Conversational Community Prototype: Scholarly Conversational Assistant},
    archivePrefix = {arXiv},
    eprint = {2001.06910},
    primaryClass = {cs.CL},
    year = {2020}
  }
  ```  

#### Less preferred format (needed for Springer)

  * Paper type is `article`!
  * Fields to include:
    - `author`
    - `title`
    - `journal = {arXiv}`
    - `volume = {cs.CL/PAPER_ID}`
    - `year`
  * Not to include: `eprint`, `primaryClass`, `url`
  * Example
  ```
  @article{Balog:2020:arXiv,
    author    = {Krisztian Balog and Lucie Flekova and Matthias Hagen and Rosie Jones and Martin Potthast and Filip Radlinski and Mark Sanderson and Svitlana Vakulenko and Hamed Zamani},
    title     = {Common Conversational Community Prototype: Scholarly Conversational
                Assistant},
    journal   = {arXiv},
    volume    = {cs.CL/2001.06910},
    year      = {2020},
  }
  ```  

### Citing books

  * Fields to include:
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
  @book{Balog:2018:Book,
    author = {Krisztian Balog},
    title = {Entity-Oriented Search},
    series = {The Information Retrieval Series},
    volume = {39},
    publisher = {Springer},
    year = {2018}
  }
  ```

### Citing PhD theses

  * Fields to include:
    - `author`
    - `title`
    - `school`
    - `year`
  * Not to include: `address`, `doi`, `isbn`, `url`, etc.
  * Example
  ```
  @phdthesis{Maxwell:2019:PhDThesis,
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
