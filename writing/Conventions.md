# Conventions on writing (and LaTeX)

## Spelling

  * **American spelling**
  * Some specific words with the chosen spelling
    - `ad hoc`
    - `behavior`
    - `dataset`
    - `judgment`
    - `labeling`
    - `learning-to-rank`
    - `modeling`
    - `normalization`
    - `use-case`
    - `semi-structured`
    - `state of the art` (noun) vs. `state-of-the-art` (adj)
    - `therefore`
  * `top x` results (not `top-x`) when x is a number (but `top-$k$`)


## Capitalization and abbreviations

  * Section/subsection headings in Title Case: `Like This and This`.
  * Capitalization of certain words:
    - `information retrieval`, `natural language processing`
    - `language modeling`
    - `intranet`
    - `web page`, `web site`, `web search`, BUT, `World Wide Web`, `Web 2.0`
  * Chapter, section, table and figure references are always capitalized: `Chapter X`, `Section X`, `Table X`, `Figure X.Y`, BUT `this chapter,` `this section`.
  * Cross-references should be written in full when they stand at the beginning of a sentence (`Chapter X`, `Section X`, etc.), otherwise abbreviated: `Chap./Chaps.`, `Sect./Sects.`, `Fig./Figs.`, `p./pp.`, `Eq./Eqs.`


## Punctuation and spacing

  * Use the [serial comma](http://en.wikipedia.org/wiki/Serial_comma); e.g., `one, two, and three` `I want no ifs, ands, or buts`
  * If a quote is followed by a dot or comma, the dot or comma should be put inside the quote
    - `one example`. => `one example.`
  * Footnotes should immediately follow the punctuation (no space between).
    - `This is a sentence.\footnote{...}`
  * Always put a comma after e.g. and i.e. E.g., `In this case, e.g., ...`
  * Never start a sentence with `i.e.,` or `e.g.,` but write out `That is,` and `For example,`.


## Formatting

  * Section numbering should be max three levels deep.
  * For sections and subsections use `Sect.~\ref{sec:xxx}``.  For subsubsections, use `\S\ref{sec:xxx}` instead of `Sect.X.Y.Z`.
  * Figures
    - `[h]` positioning should be avoided. All figures and tables should float to top.
  * URLs in footnotes: `\footnote{\url{http://xxx.xx.xx}}`
  * Use `\emph` for emphasizing text (not `\textit`!)
  * Quotes: use \`\` and \'\' instead of \' and \'


## Equations and math

  * Number only those equations that are referenced later in the text. For the others, use `equation*`
  * It is preferred to put the `label` tag after the actual formula, before the `\end{equation}` tag
  * Use `\eqref` instead of `\ref` when referring to equations
    - You'll need the `amspath` package for this: `\usepackage{amsmath}`
  * At the beginning of sentences write `Equation (1.45)`
  * In other places it is sufficient to use the equation number set in parentheses, e.g., `(1.45)`, but the abbreviations Eq./Eqs. may also be used (but Eqn. is not!)
  * Ranked lists should always be `(...)` not `<...>`.
  * Put a `%` before and after figures and equations for better separation from the text, like
```
%
\begin{equation}
...
\end{equation}
%
```

## References

  * Use [natbib](https://www.overleaf.com/learn/latex/natbib_citation_styles).
  * Know the difference between `\citep{..}` and `\citet{..}`.
    - `\citet{}` is for textual citation. E.g., `\citet{Smith:2000:ABC} proposed ...` => `Smith et al. (2000) proposed...`
    - `\citep{}` is parenthetical citation. E.g., `In \citet{Smith:2000:ABC} the idea of ...` => `In [2] the idea of...`
    - Never write out `Smith et al.`, there is a `\citeauthor{}` command for that (but most likely what you're looking for is actually `\citet{}`).
  * Bib keys: `author:year:FTL` (where FTL are first three capital letters from the title). E.g., `Balog:2012:ERL`, `Meij:2012:ASM`.
  * The shortened format for conference papers is: `Proc. of XXX, pages zz-zz, YYYY.`
    - That is, space before 'YY, no publisher, address, etc.
    0 The exception is TREC papers, where the year is one year behind the proceedings date. So for TREC papers us `Proc. of TREC 'YY`, YY+1.
  * For workshops, it is: `In Proc. of NAME_OF_THE_WORKSHOP, pages zz-zz, YYYY.`
    - That is, no workshop acronym, publisher, etc.

## LaTeX

  * **The page should compile without warnings!**
    - That is, if you see `LaTeX Warning: There were undefined references.` or `LaTeX Warning: There were multiply-defined labels.` in the output, those must be fixed!
