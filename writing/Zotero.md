# Zotero

  * We recommend using [Zotero](https://www.zotero.org/) (a free, open-source reference management software) to manage your bibliography and generate BibTeX entries.

  * Zotero's default export format is not compatible with our BibTeX conventions. You must use the Better BibTeX export format (see the [Better BibTeX documentation](https://retorque.re/zotero-better-bibtex/exporting/))
    - Download the [latest release](https://github.com/retorquere/zotero-better-bibtex/releases/tag/v6.7.63)
    - In Zotero, go to Tools > Add-ons > Install Add-on From File… and select the downloaded file.

    - [Here](resources/zotero-config.json) is a configuration file that can be imported into Zotero to set up the correct citation style and export options.
  <!-- make a quote -->
    - Group sharing:
      + We use Zotero groups to manage our references. A new group is created for each project. The group is shared with all the members of the project.
      + Note that group libraries are wholly separate from My Library. Any items dragged into them are separate copies and changes to the items will not be reflected in your own copy of the item until you drag it back into My Library.

## Automatic Export
  
    * Zotero can automatically export your bibliography (collection) to a .bib file when you add a new reference.
    * Note that the automatic export will only work if you have the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) plugin installed.
    * To automatically push to GitHub:
      - Clone the repository to your local machine.
      - In Zotero, right-click on the collection to export and choose “Export Collection…” with Better BibTeX’s export translators (e.g., “Better BibTeX”). Make sure the `Keep updated` option is selected.
      - Select the `<bibliography>.bib` file in the repository as the export location.
      - Inside the repository folder, run `git config zotero.betterbibtex.push true`
    * **Note** If using Overleaf, you will need to manually pull the changes from GitHub.
