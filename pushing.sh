#!/bin/bash
# This script pushes all branches to GitHub, Synology, or both.

# Remotes: 'github' and 'origin' (Synology)

echo "Select an option:"
select option in "GitHub" "Synology" "Both"; do
    case $REPLY in
        1) remotes=("github"); break;;
        2) remotes=("synology"); break;;
        3) remotes=("github" "synology"); break;;
        *) echo "Invalid option. Please select 1, 2, or 3.";;
    esac
done

git add .

read -p "Please type the commit message: " message

git commit -m "$message"

for remote in "${remotes[@]}"; do
    echo "Pushing to $remote..."
    git push "$remote" --all
done
