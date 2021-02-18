# LaTeX conventions

## Typesetting

  * Unless stated otherwise, typesetting is done using the `pdflatex` engine and with `BibTeX` as the bibliography engine.
  * **Changes may only be pushed to github if the document compiles without warnings!**
    - Typical warnings include `There were undefined references` and `There were multiply-defined labels`.

## Referencing

  * When referencing document elements (chapters, sections, tables, figures), use an unbreakable space `~` before the `\ref` command to avoid the number breaking into a new line on its own. For example:
    - `Section~\ref{sec:xxx}`
    - `Fig.~\ref{fig:xxx}`

## Formatting

  * Quotes: use double quotes as \`\` .. \'\' (instead of \" ... \") to be rendered as curved quotation marks (i.e., \`-s on the left side instead of straight \'-s)
  * Use `\emph` for emphasizing text (not `\textit`!)
  * URLs in footnotes: `\footnote{\url{http://xxx.xx.xx}}`
  * Do not indent paragraphs after item lists and equations. This can be achieved by either using `%` (as opposed to an empty line) as separator or explicitly adding `\noindent`.

## Sections

  * Section numbering should be max three levels deep. For headings deeper than that, use `\paragraph{xxx}` or boldfacing.
  * When referring to sections and subsections, use `Section~\ref{sec:xxx}` or `Sect.~\ref{sec:xxx}`.  Subsubsections may also be referred to as `\S\ref{sec:xxx}`.

## Figures and tables

  * `[h]` positioning should be avoided. All figures and tables should float to top.
  * Captions are placed above tables and below figures.

## Item lists

  * Indent items in the source file.
  * Use either empty lines or `%` above and below item environments for better separation from the text.

## Equations and math

  * Number only those equations that are referenced later in the text. For non-numbered equations, use the `equation*` environment.
  * It is preferred to put the `label` tag after the actual formula, before the `\end{equation}` tag
  * Use `\eqref` instead of `\ref` when referring to equations
    - You'll need the `amspath` package for this: `\usepackage{amsmath}`
  * At the beginning of sentences write `Equation (1.45)`
  * In other places it is sufficient to use the equation number set in parentheses, e.g., `(1.45)`, but the abbreviations Eq./Eqs. may also be used (but Eqn. is not!)
  * Ranked lists should always be `(...)` not `<...>`.
  * Put a `%` before and after equations for better separation from the text, like
```
%
\begin{equation}
...
\end{equation}
%
```
