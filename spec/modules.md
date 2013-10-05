Modules
=======
Django Git will be split into multiple submodules to allow for different parts
to be reusable accross different projects.  The primary goal is to have all of
the submodules usuable within the Django Git project, but a single core module
would create a cluttered setup very quickly.

Users
=====
- username
- password

Repositories
============
- owner (GFK)
  - owner_id
  - owner_ct
    - type "User"
  - reverse "repositories"
- name

Commits
=======
- repository
- sha_hash
- parents
  - type "Commit"
  - Many to many
  - Reverse "children"

Issues
======
- creator
  - type "User"
  - reverse "created_issues"
- repository
  - type "Repository"
  - reverse "issues"
- subject
- details

Directory structure
===================

django_git/
    auth
        User
    repositories
        Repository
        Commit
    issues
        Issue
