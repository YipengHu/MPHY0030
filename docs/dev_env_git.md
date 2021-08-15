# Work with Git
- This document introduces some basic usage of [Git](https://git-scm.com/), a distributed versioning system for tracking and managing source code changes during software development. 
- [WEISSLab](http://weisslab.cs.ucl.ac.uk/) and [GitHub](https://github.com/) are two project hosting services. The [module repository](https://weisslab.cs.ucl.ac.uk/yipenghu/mphy0030) is hosted on the former, while you will submit your coursework to the latter. 
- For more information and tutorial, have a look at the book/documentation [*Pro Git*](https://git-scm.com/book/en/v2).


## Install Git
Many linux distributions including those on WSL have Git pre-installed. Type `git --help` to see if it is the case. If not, please follow the [Git book](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install and get started.

## Clone the module repository on WEISSLab
Make a local copy of the entire repository hosted on the remote WEISSLab, e.g. remote repository -> local repository.
```bash
git clone https://weisslab.cs.ucl.ac.uk/yipenghu/mphy0030
```

Change the current directory to the repository folder, then update to the latest code.
```bash
cd mhy0030
git pull
```

## Complete the module coursework on GitHub

### Set up a GitHub account
If you do not have one, sign up for a GitHub account at [github.com](https://github.com/).

### Create a repository
[Create a repo](https://docs.github.com/en/free-pro-team@latest/articles/create-a-repo) with name `mphy0030-coursework`.

### Record you progress
Git supports complex workflows for large professional software development projects. A (over-)simplified single-user project may only need a few steps/commands.
- Make changes to your code on your local repository.
- Add the changes (or new files) to Git, so they become tracked.
- Commit these changes with a commit message.
- Push the commits to the remote repository.

```bash
git add files_that_with_changes
git commit -m "a brief message summarise the committed changes"
git push origin main
```

> For those adopt paired-coding, the workflow is likely to be more complex and [branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) will become handy.
