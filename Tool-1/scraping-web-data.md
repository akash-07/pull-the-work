**Connection links**

pull-requests: GET /repos/:owner/:repo/pulls

key: `commits_url`-> gives you commits of the PR

key: `url` -> takes you to the specific PR    

When to go the specific url:
- `title` -> gets you the PR message
- `commits_url` -> gets you commit url
- `commits` -> commit count
- `additions` -> Number of lines added
- `deletions` -> Number of lines deleted
- `changed_files` -> Number of files changed
- `author_association` -> Says CONTRIBUTOR if the submitter is a contributor

Right now I am just concerned about the title of the pull request. I will look into user information later.
