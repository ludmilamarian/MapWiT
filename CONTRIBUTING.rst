Contribution guide
==================

Interested in contributing to the MapWiT project? There are lots of ways to
help.

.. rubric:: Code of conduct

Overall, we're **open, considerate, respectful and good to each other**. We
contribute to this community not because we have to, but because we want to.
If we remember that, our `code-of-conduct` will come naturally.


Types of contributions
----------------------

Contribute Data
~~~~~~~~~~~~~~~
**How to appear on the map.** This application was build as a demo, and the
most common type of contribution is a `data file`. Starting from the existing
example, you can add a new data file directly on GitHub, and make a Pull Request
with the new data file. Once merged, the data will be part of the application,
and will be displayed on the map.

Report bugs
~~~~~~~~~~~
- **Found a bug? Want a new feature?** Open a GitHub issue on the
  repository and get the conversation started (do search if the issue has
  already been reported).

- **Found a security issue?** Alert the maintainer privately, this will allow
  the security patching before potential attackers look at the issue.

Translate
~~~~~~~~~
**Missing your favourite language?** MapWiT currently does not contain much
text but if you feel a translation would be useful, please get in touch.

Write documentation
~~~~~~~~~~~~~~~~~~~
- **Found a typo?** You can edit the file and submit a pull request directly on
  GitHub.

- **Debugged something for hours?** Spare others time by writing up a short
  troubleshooting issue, and label it accordingly.

- **Wished you knew earlier what you know now?** Help write both non-technical
  and technical guides.

Write code
~~~~~~~~~~
**Want to contribute?** Either start from an existing issue on the repository's
GitHub page, or add a new issue to work on. Once ready, make a Pull Request (PR),
and the maintainer will take a look. If you are unsure about the development,
get in touch first.


Commit messages
~~~~~~~~~~~~~~~
Commit message is first and foremost about the content. You are communicating
with fellow developers, so be clear and brief.

(Inspired by `How to Write a Git Commit Message <https://chris.beams.io/posts/git-commit/>`_)

1. `Separate subject from body with a blank line <https://chris.beams.io/posts/git-commit/#separate>`_
2. `Limit the subject line to 50 characters <https://chris.beams.io/posts/git-commit/#limit-50>`_
3. Indicate the component follow by a short description
4. `Do not end the subject line with a period <https://chris.beams.io/posts/git-commit/#end>`_
5. `Use the imperative mood in the subject line <https://chris.beams.io/posts/git-commit/#imperative>`_
6. `Wrap the body at 72 characters <https://chris.beams.io/posts/git-commit/#wrap-72>`_
7. `Use the body to explain what and why vs. how, using bullet points <https://chris.beams.io/posts/git-commit/#why-not-how>`_

For example::

    component: summarize changes in 50 char or less

    * More detailed explanatory text, if necessary. Formatted using
      bullet points, preferably `*`. Wrapped to 72 characters.

    * Explain the problem that this commit is solving. Focus on why you
      are making this change as opposed to how (the code explains that).
      Are there side effects or other unintuitive consequences of this
      change? Here's the place to explain them.

    * The blank line separating the summary from the body is critical
      (unless you omit the body entirely); various tools like `log`,
      `shortlog` and `rebase` can get confused if you run the two
      together.

    * Use words like "Adds", "Fixes" or "Breaks" in the listed bullets to help
      others understand what you did.

    * If your commit closes or addresses an issue, you can mention
      it in any of the bullets after the dot. (closes #XXX) (addresses
      #YYY)

Pull requests
-------------
Need help making your first pull request? Check out the GitHub guide
`Forking Projects <https://guides.github.com/activities/forking/>`_.

.. rubric:: Work in progress (WIP)

Do publish your code as pull request sooner than later. Just prefix the pull
request title with ``WIP`` (=work in progress) if it is not quite ready.

.. rubric:: Allow edits from maintainers

To speed up the integration process, it helps if on GitHub you
`allow maintainers to edit your pull request <https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/>`_
so they can fix small issues autonomously.
