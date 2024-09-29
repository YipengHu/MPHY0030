# Work with Git
- This document introduces some basic usage of [Git](https://git-scm.com/), a distributed versioning system for tracking and managing source code changes during software development. 
- [GitHub](https://github.com/) is a project hosting service, on which this module repository is hosted, while you will submit your coursework to the latter. 
- For more information and tutorial, have a look at the book/documentation [*Pro Git*](https://git-scm.com/book/en/v2).


## Install Git
Many linux distributions including those on WSL have Git pre-installed. Type `git --help` to see if it is the case. If not, please follow the [Git Book](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install and get started.

## Clone the module repository on GitHub
Make a local copy of the entire repository hosted on the remote GitHub, e.g. remote repository -> local repository.
```bash
git clone https://github.com/yipenghu/MPHY0030.git
```

Change the current directory to the repository folder, then update to the latest code.
```bash
cd mphy0030
git pull
```

## Optional: Complete the module coursework on GitHub

### Set up a GitHub account
If you do not have one, sign up for a GitHub account at [github.com](https://github.com/).

### Create a repository
[Create a repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories) with a repository name, e.g. `mphy0030-coursework`.

### Record you progress
Git supports complex workflows for large professional software development projects. A simplified single-user project may only need a few steps/commands.
- Make changes to your code on your local repository.
- Add the changes (or new files) to Git, so they become tracked.
- Commit these changes with a commit message.
- Push the commits to the remote repository.

```bash
git add files_that_with_changes
git commit -m "a brief message summarise the committed changes"
git push origin main
```

> For those adopt paired-coding, the workflow is likely to be more complex and [branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) will become useful.
