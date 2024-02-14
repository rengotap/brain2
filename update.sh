echo "You are on" $(hostname)
changed=false

# If the response from 
git remote update && git status -uno | grep -q 'Your branch is behind' && changed=true
if [ $changed = true ]; then
    git pull
    echo "Updated successfully";
else
    echo "Updating Remote"
    git add --all
    git commit --all -m "Repo Sync from $(hostname)"
fi
# if git status up to date then push, if not then pull
read message