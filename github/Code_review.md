# Code review guidelines

Read the [Google code review guidelines](https://github.com/google/eng-practices) for a general overview on best review practices. 
Below are our internal rules.

## What to do as an author

  * Find a person to review.
  * Wait for feedback. (Ping the person, if necessary.)
  * Address the review comments.
    - Respond to each comment or say "Done". 
    - Mark comment threads that have been fully addressed as "resolved". If there’s an open reply, an open thread, a suggestion, or a question, the thread should be left to be resolved by the reviewer.
  * Request a new review from the reviewer once you have addressed all their comments.
  * Once approved, merge the PR to main and delete the branch.
    - Note: squash merging should be the default behavior; if not, update repo settings (disable other merge options)

## What to do as a reviewer

  * Code reviews are expected to be performed within hours, not days.  Respond if you're unavailable so that the author can find someone else to do the review.
  * Check the PR and leave comments using the GitHub interface.
    - The submitted code is assumed to pass the tests.  You don't need to check out or run it.  If you think the code doesn't work as intended, ask for additional tests (be specific).
  * If you had earlier comments that needed a response or action from the author, it is your responsibility to mark the comment thread as resolved.
  * Once you're done, there are three possible actions:
    - Comment: you're waiting for a response on an initiated or ongoing conversation.
    - Approve: by giving an "LGTM", you approve merging the PR into main; there may be additional changes requested, which do not need review.
    - Request changes: you ask for meaningful changes that will need to be reviewed again.

### Things to look out for

  * Docstrings
    - There should be docstrings for files, classes, and methods.
    - Exceptions: @property methods
  * Compliance with style guide regarding formatting and naming conventions, import ordering, etc.
  * Test coverage

## Things to remember

  * Be kind.
  * Assume everyone is intelligent and well-meaning.
  * Ask questions; don’t make demands. 
  * Accept that many programming decisions are opinions. Discuss tradeoffs, which you prefer, and reach a resolution quickly.
