import os
import time
import subprocess

# Path to your local Git repository
repo_path = r"F:\git_auto_commit"  # Replace this with your repo path

# Change to the repo directory
os.chdir(repo_path)

# Dummy file to modify/create
file_name = "dummy_commit.txt"

# Write a timestamp to the dummy file (Python 2.7 compatible)
with open(file_name, "w") as file:
    file.write("Automated commit: " + str(time.ctime()))

# Git commit and push sequence
try:
    # Stage the changes
    subprocess.call(["git", "add", file_name])
    
    # Commit the changes
    commit_message = "Automated commit: " + str(time.ctime())
    subprocess.call(["git", "commit", "-m", commit_message])
    
    # Push the changes to GitHub
    subprocess.call(["git", "push", "origin", "main"])
    print("Successfully committed and pushed to GitHub!")
    
except subprocess.CalledProcessError as e:
    print("An error occurred: %s" % e)
