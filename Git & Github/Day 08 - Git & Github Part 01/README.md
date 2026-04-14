<div align="center">
<h1>Git & Github Part 01</h1>
</div>

# Context

- [Context](#context)
  - [Git \& GitHub](#git--github)
    - [What is Git?](#what-is-git)
    - [What is Version Control?](#what-is-version-control)
      - [Types](#types)
    - [What Can Version Control Do?](#what-can-version-control-do)
    - [Popular Version Control Systems](#popular-version-control-systems)
    - [Inventor of Git](#inventor-of-git)
  - [Git Setup](#git-setup)
    - [Install Git](#install-git)
    - [GitHub Setup](#github-setup)
    - [Create Repository](#create-repository)
  - [Git Configuration](#git-configuration)
    - [Local vs Global Config](#local-vs-global-config)
      - [Local](#local)
      - [Global](#global)
  - [Git Workflow](#git-workflow)
    - [Staging vs Commit](#staging-vs-commit)
      - [Staging](#staging)
      - [Commit](#commit)
    - [Commit Structure](#commit-structure)
  - [Git History](#git-history)
    - [Git Log](#git-log)
    - [Useful Git History Commands](#useful-git-history-commands)
    - [Diff](#diff)
    - [Revert](#revert)
    - [Push](#push)

## Git & GitHub

### What is Git?

- Git is a **popular version control system** used in software development.
- It is:

  - Open source
  - Scalable
  - Widely used in industry

---
[⬆️ Go to Context](#context)

### What is Version Control?

- A system to manage changes in files, programs, and directories.

#### Types

- Centralized (e.g., SVN, Perforce)
- Distributed (e.g., Git, Mercurial)

---
[⬆️ Go to Context](#context)

### What Can Version Control Do?

- Track files in different states
- Combine different versions of files
- Identify specific versions
- Revert changes when needed

---
[⬆️ Go to Context](#context)

### Popular Version Control Systems

- Git → Distributed, most widely used
- Subversion (SVN) → Centralized, simple workflow
- Mercurial → Distributed, beginner-friendly
- CVS → Older centralized system
- Perforce (Helix Core) → Enterprise-level centralized system
- Bazaar → Simple distributed system
- Monotone → Focus on integrity and simplicity

---
[⬆️ Go to Context](#context)

### Inventor of Git

> **Linus Torvalds**

- Created Linux kernel (1991)
- Created Git (2005) for Linux development management
- Other projects:

  - Subsurface (diving software)
  - Audio noise experimentation

---
[⬆️ Go to Context](#context)

## Git Setup

### Install Git

- [https://git-scm.com/install/windows](https://git-scm.com/install/windows)

  ```sh
  git --version
  ```

### GitHub Setup

- [https://github.com/login](https://github.com/login)

---
[⬆️ Go to Context](#context)

### Create Repository

- A repository (repo) is a directory containing:

  - Files
  - Sub-directories
  - Git history

⚠️ Do not edit `.git` folder manually

- Create repo locally:

  ```sh
  git init
  ```

- Clone existing repo:

  ```sh
  git clone <repo-url>
  ```

---
[⬆️ Go to Context](#context)

## Git Configuration

### Local vs Global Config

#### Local

- Used when working on shared or temporary machines

  ```sh
  git config --local user.name "Your Name"
  git config --local user.email "your@email.com"
  ```

#### Global

- Used on personal machine

  ```sh
  git config --global user.name "Your Name"
  git config --global user.email "your@email.com"
  ```

- Check config:

  ```sh
  git config --list
  git config --global --list
  git config --local --list
  ```

Notes:

- Use GitHub username and email
- Check Windows credential manager if needed

---
[⬆️ Go to Context](#context)

## Git Workflow

- Modify files
- Stage changes
- Commit changes
- Push to remote repository

- Full workflow commands:

  ```sh
  git status
  git add .
  git commit -m "your message"
  git push origin main
  ```

---
[⬆️ Go to Context](#context)

### Staging vs Commit

#### Staging

- Preparing files for commit

  ```sh
  git add file.txt
  git add .
  ```

#### Commit

- Saving snapshot of changes

  ```sh
  git commit -m "your message"
  ```

---
[⬆️ Go to Context](#context)

### Commit Structure

- Each commit contains:

  - Unique ID
  - Message
  - Timestamp
  - Changes

- View commit details:

  ```sh
  git show
  ```

---
[⬆️ Go to Context](#context)

## Git History

### Git Log

- Shows commit history
- Can become long and complex

  ```sh
  git log
  ```

- Cleaner view:

  ```sh
  git log --oneline --graph --all
  ```

---
[⬆️ Go to Context](#context)

### Useful Git History Commands

- View logs
- Filter by time
- View specific commit details
- Compare commits (diff)

  ```sh
  git log --since="2 days ago"
  git log --author="name"
  git show <commit-id>
  ```

---
[⬆️ Go to Context](#context)

### Diff

- Shows differences between versions
- Helps track changes

  ```sh
  git diff
  git diff <commit-id>
  git diff file.txt
  ```

---
[⬆️ Go to Context](#context)

### Revert

- Used to undo changes safely

  ```sh
  git revert <commit-id>
  ```

---
[⬆️ Go to Context](#context)

### Push

- Sends local commits to remote repository

  ```sh
  git push origin main
  ```

- First time push (set upstream):

  ```sh
  git push -u origin main
  ```

---
[⬆️ Go to Context](#context)
