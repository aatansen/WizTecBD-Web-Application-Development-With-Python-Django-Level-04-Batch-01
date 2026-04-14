<div align="center">
<h1>Git & Github Part 02</h1>
</div>

# Context

- [Context](#context)
  - [Branching](#branching)
  - [What is a Branch?](#what-is-a-branch)
    - [Branch Characteristics](#branch-characteristics)
    - [Branch Operations](#branch-operations)
    - [Branch Conflicts](#branch-conflicts)
  - [Fetch, Merge, Pull](#fetch-merge-pull)
  - [Push / Pull Workflow](#push--pull-workflow)
  - [Stash](#stash)
  - [Merge Strategies](#merge-strategies)
  - [Git Rebase](#git-rebase)
  - [Merge vs Rebase vs Squash](#merge-vs-rebase-vs-squash)
  - [Advanced Git Tools](#advanced-git-tools)
  - [GitHub Features](#github-features)
  - [Bonus Topics](#bonus-topics)

## Branching

## What is a Branch?

- A branch is an independent version of a repository
- Used for parallel development

- Check current branch:

  ```sh
  git branch
  ```

- See all branches (including remote):

  ```sh
  git branch -a
  ```

---
[⬆️ Go to Context](#context)

### Branch Characteristics

- Files may differ between branches
- Some files may not exist in all branches
- Enables multiple workflows

- Switch between branches:

  ```sh
  git checkout <branch-name>
  ```

- Modern way:

  ```sh
  git switch <branch-name>
  ```

---
[⬆️ Go to Context](#context)

### Branch Operations

- Create branch
- Merge branch
- Delete branch
- Remote branch management

- Create branch:

  ```sh
  git branch new-feature
  ```

- Create + switch:

  ```sh
  git checkout -b new-feature
  ```

- Modern:

  ```sh
  git switch -c new-feature
  ```

- Delete branch:

  ```sh
  git branch -d new-feature
  ```

- Force delete:

  ```sh
  git branch -D new-feature
  ```

- Push branch to remote:

  ```sh
  git push origin new-feature
  ```

- Delete remote branch:

  ```sh
  git push origin --delete new-feature
  ```

---
[⬆️ Go to Context](#context)

### Branch Conflicts

- Occur when multiple changes affect same file
- Must be resolved manually

- After conflict:

  ```sh
  git status
  ```

- Mark resolved:

  ```sh
  git add .
  git commit
  ```

---
[⬆️ Go to Context](#context)

## Fetch, Merge, Pull

- Fetch → Get updates from remote
- Merge → Combine changes
- Pull → Fetch + Merge (automatic)

  ```sh
  git fetch
  git merge origin/main
  git pull
  ```

- Pull specific branch:

  ```sh
  git pull origin main
  ```

---
[⬆️ Go to Context](#context)

## Push / Pull Workflow

- Pull latest changes
- Make changes
- Commit
- Push updates

  ```sh
  git pull
  git add .
  git commit -m "your message"
  git push
  ```

---
[⬆️ Go to Context](#context)

## Stash

- Temporarily saves changes without committing
- Useful when switching tasks

  ```sh
  git stash
  ```

- View stashes:

  ```sh
  git stash list
  ```

- Apply stash:

  ```sh
  git stash apply
  ```

- Apply + remove:

  ```sh
  git stash pop
  ```

- Drop stash:

  ```sh
  git stash drop
  ```

---
[⬆️ Go to Context](#context)

## Merge Strategies

- Different ways to combine branches
- Can preserve or simplify history

- Default merge:

  ```sh
  git merge feature-branch
  ```

- No fast-forward (keep history):

  ```sh
  git merge --no-ff feature-branch
  ```

- Abort merge:

  ```sh
  git merge --abort
  ```

---
[⬆️ Go to Context](#context)

## Git Rebase

- Rewrites commit history
- Used for cleaner linear history
- Can squash commits

  ```sh
  git rebase main
  ```

- Interactive rebase:

  ```sh
  git rebase -i HEAD~3
  ```

- Abort rebase:

  ```sh
  git rebase --abort
  ```

- Continue after conflict:

  ```sh
  git rebase --continue
  ```

---
[⬆️ Go to Context](#context)

## Merge vs Rebase vs Squash

- Merge → Keeps history
- Rebase → Linear history
- Squash → Combines commits

- Squash during merge:

  ```sh
  git merge --squash feature-branch
  ```

- Squash via rebase:

  ```sh
  git rebase -i HEAD~3
  ```

---
[⬆️ Go to Context](#context)

## Advanced Git Tools

- Cherry-pick → Apply specific commits
- Amend → Modify last commit
- Filter-repo → Clean or rewrite history

  ```sh
  git cherry-pick <commit-id>
  ```

  ```sh
  git commit --amend
  ```

- Change last commit message:

  ```sh
  git commit --amend -m "new message"
  ```

- (Advanced) rewrite history:

  ```sh
  git filter-repo
  ```

---
[⬆️ Go to Context](#context)

## GitHub Features

- Repository hosting
- Forking projects
- Issues tracking
- Pull requests
- Project management tools
- README documentation
- CI/CD integration

- Add remote:

  ```sh
  git remote add origin <repo-url>
  ```

- View remotes:

  ```sh
  git remote -v
  ```

- Fork workflow (after cloning fork):

  ```sh
  git remote add upstream <original-repo-url>
  git fetch upstream
  git merge upstream/main
  ```

---
[⬆️ Go to Context](#context)

## Bonus Topics

- Conventional commits
- GUI tools for Git

- Example commit:

  ```sh
  git commit -m "feat: add login system"
  git commit -m "fix: resolve bug in auth"
  ```

---
[⬆️ Go to Context](#context)
