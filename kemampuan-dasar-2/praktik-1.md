# Create a folder for your project.
mkdir rhymes
cd rhymes

# To make this directory and empty Git repo do this:
git init

# I usually create an empty README.txt file for the first commit in my project
# history.
touch README.txt
git add README.txt
git commit -m 'First commit.'

# Add some explanation about the project to the README file.
echo 'This repo is a collection of my favorite nursery rhymes.' >> README.txt

# Review uncommitted changes. Then commit them.
git status
git diff
git add README.txt
git commit -m 'Added project overview to README.txt'
# Alice downloads favorite rhymes.
wget https://www.acquia.com/sites/default/files/blog/all-around-the-mulberry-bush.txt
wget https://www.acquia.com/sites/default/files/blog/jack-and-jill.txt
wget https://www.acquia.com/sites/default/files/blog/old-mother-hubbard.txt
wget https://www.acquia.com/sites/default/files/blog/twinkle-twinkle.txt
wget https://www.acquia.com/sites/default/files/blog/hokey-pokey.txt

# The files have been downloaded, but not committed.
# You can see this with git status. git status
# Alice adds the files one-by-one to make her git history look nice and tidy.
git add all-around-the-mulberry-bush.txt
git status
git commit -m 'Added all-around-the-mulberry-bush.txt.'
git add jack-and-jill.txt
git commit -m 'Added jack-and-jill.txt.'

# Alice gets lazy and decides to just add everything else at once.
git add .
git commit -m 'Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt'

# Alice reviews and admires her commit history.
git log
git log --oneline
git log -p
git remote add origin https://github.com/bryanhirsch/rhymes.git
git push -u origin master


# First Bob clones his fork of Alice's rhymes project.
# (If you're following along, replace bryanhirsch below with your own GitHub username.)
git clone https://github.com/bryanhirsch/rhymes.git
cd rhymes

# To keep things simple and tidy, Bob will keep the master branch in sync with Alice's version of the master branch.
# Bob creates a new branch, where he will store his changes.
git checkout -b hickory-dickory

# Add Hickory Dickory Dock to the repo.
wget https://www.acquia.com/sites/default/files/blog/hickory-dickory-dock.txt...
add hickory-dickory-dock.txt
git commit -m 'Added hickory-dickory-dock.txt.'

# Bob pushes the changes from his local copy of rhymes up to GitHub.
git push origin hickory-dickory


# Alice renames origin -> alice.
cd rhymes
git remote rename origin alice

# Add a remote pointing to Bob's copy of the project.
git remote add bob https://github.com/bryanhirsch/rhymes.git

# Review remotes.
git remote

# Confirm each remote points to the correct repository.
git remote -v

# Fetch a copy of Bob's work.
git fetch bob

# Review all the branches (both local and remote).
git branch -a

# Check out a local copy of Bob's work and review it.
git checkout -b hickory-dickory bob/hickory-dickory
git diff master hickory-dickory
git log -1 -p

# Checkout master and merge Bobs changes in.
git checkout master
git merge hickory-dickory

# Push changes up to GitHub git push alice master
# Remove our local copy of the hickory-dickory branch. We don't need it anymore.
git branch -D hickory-dickory