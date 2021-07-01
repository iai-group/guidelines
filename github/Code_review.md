# Code review guidelines

## What to do as an author

  * Find a person to review
  * Wait for feedback
  * Address the review comments
    - Respond to each comment or say "Done"
    - Re-request review
  * Once approved, merge the PR to main and delete the branch
    - Note: squash merging should be the default behavior; if not, update repo settings (disable other merge options)

## What to do as a reviewer

  * Code reviews are expected to be performed within hours, not days.  Respond if you're unavailable so that the author can find someone else to do the review.
  * Check the PR and leave comments using the GitHub interface.
    - The submitted code is assumed to pass the tests.  You don't need to check out or run it.  If you think the code doesn't work as intended, ask for additional tests (be specific).
  * Once you're done, there are three possible actions:
    - Comment: you're waiting for a response on an initiated or ongoing conversation.
    - Approve: you approve merging the PR into main; there may be additional changes requested, which do not need review.
    - Request changes: you ask for meaningful changes that will need to be reviewed again.
  * If the author responds to comments raised by the reviewer, and the conversation is resolved, mark it as such, using the "Resolve conversation" button.

### Things to look out for

  * Docstrings
    - There should be docstrings for files, classes, and methods.
    - Exceptions: @property methods
  * Compliance with style guide regarding formatting and naming conventions, etc.
