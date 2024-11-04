# git add .
# git commit -m "Message"
# git push
# https://github.com/aceprasad3911/WFinal_Assesment_CPS5002.git
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Branches:
# Main Branch (main or master):
# This branch should always contain stable, production-ready code. Any code that is merged into this branch should be thoroughly tested and reviewed.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Development Branch (develop):
# This branch acts as an integration branch for features. Developers can merge their feature branches into this branch once they are complete. It serves as a staging area for testing before merging into the main branch.
# e.g. 1) Starting Development:
# git checkout develop
# git checkout -b feature/new-bot-type
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Feature Branches:
# Each new feature or enhancement should be developed in its own branch. Naming convention could be something like feature/description, e.g., feature/bot-enhancements, feature/scavenger-swarm-logic.
# This keeps features isolated and allows for easier management of changes. Once a feature is complete and tested, it can be merged back into the develop branch.
# e.g. 2) Developing the Feature:
# git add .
# git commit -m "Add new bot type with enhanced capabilities"
# git push origin feature/new-bot-type
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Testing/Code/Review:
# Once the feature is complete, create a pull request (PR) to merge the feature branch into develop.
# Team members can review the code, suggest changes, and run tests.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Merging:
# After approval, merge the feature branch into develop:
# e.g. 3: Merging Branches:
# git checkout develop
# git merge feature/new-bot-type
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Bugfix Branches:
# When a bug is found, create a branch specifically for fixing that bug, named something like bugfix/description, e.g., bugfix/fix-recharge-station-issue.
# Similar to feature branches, once the bug is fixed and tested, it can be merged into develop.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Release Branches:
# When preparing for a new release, you can create a branch from develop, named something like release/v1.0.0.
# This branch is used to finalize the release, allowing for last-minute bug fixes and documentation updates. Once the release is ready, it can be merged into both main and develop.
# e.g. 4) Preparing for Release:
# git checkout develop
# git checkout -b release/v1.0.0
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Hotfix Branches:
# For urgent fixes that need to be addressed in production immediately, create a hotfix branch from main, named hotfix/description, e.g., hotfix/fix-critical-bug.
# After fixing the issue, merge the hotfix back into both main and develop to ensure that the fix is included in future releases.
# e.g. 5) Handling Bugs:
# git checkout main
# git checkout -b hotfix/fix-bug
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


