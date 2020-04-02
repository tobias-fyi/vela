#!/bin/bash
setup_git() {
  git config --global user.email "mst10041967@gmail.com"
  git config --global user.name "Rohit Tanwar"
}

commit_website_files() {
  if [ $TRAVIS_EVENT_TYPE != "pull_request" ]; then
    if [ $TRAVIS_BRANCH == "master" ]; then
      git checkout master
      echo "Committing to master branch..."
      git add -A
      echo "All files added"
      git status
      if [ $TRAVIS_EVENT_TYPE == "cron" ]; then
        git commit --message "Travis build: $TRAVIS_BUILD_NUMBER [cron]"
      elif [ $TRAVIS_EVENT_TYPE == "api" ]; then
        git commit --message "Travis build: $TRAVIS_BUILD_NUMBER [custom]"
      else
        git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
      fi
      echo "Files commited"
      git status
    fi
  fi
}

upload_files() {
  if [ $TRAVIS_EVENT_TYPE != "pull_request" ]; then
    if [ $TRAVIS_BRANCH == "master" ]; then
      echo "Pushing to master branch..."
      git push --force  "https://${GH_TOKEN}@github.com/kriadmin/30-seconds-of-python-code.git" master > /dev/null 2>&1
      echo "Pushing done"
      echo "Pushing to website"
      git subtree push --prefix website "https://${GH_TOKEN}@github.com/kriadmin/30-seconds-of-python-code.git" website
      echo "Pushed to master branch"
      git status
    fi
  fi
}

setup_git
commit_website_files
upload_files
