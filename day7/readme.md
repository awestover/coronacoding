--- 
title: day 7
author: Alek Westover
---

Today you are going to learn how to use your computer and stuff!
Specifically we will be talking about the following:

- How to use your terminal
  - how to manage your file system with your terminal
  - how to run programs with your terminal
  - how to use the python/ipython shell
- How to do version control
  - git
    - git cli
  - github
- How to use a package manager 
  - installing brew for mac ppl, and using it to download 
  - e.g. installing a better terminal:
  - `brew install cask`
  - `brew cask install iterm2`
- Make a "big" project (i.e. project with multiple files) in `python`


# Terminal Usage

First open your terminal application. (powershell on windows, terminal on mac / linux)

**Useful commands:**

- pwd (print working directory)
- ls (list directory contents)
- cd (change directory)
- mv (move)
- cp (copy)
- rm (remove)
- touch (make a file)
- cat (print file contents)
- mkdir (make a directory)

On Mac you can type `man cp` (for instance) to learn what a command does, or you can google it.

# Problem 1
Make a directory with a bunch of subdirectories and have each of those have a bunch of subdirectories with files in them. Do it with the terminal, explore it with `ls / cd` and `mv`. Also look at it in your IDE and in your finder/ file explorer.

# Problem 2
Navigate to a directory where you have some coronacodingclub code stored. 
Run it with python from the terminal.

# Problem 3
Type `python / python3` in your terminal. You are now in the python shell.
This is a different environment from the rest of the terminal (type `exit()` to exit the python shell). 
In the python shell you can run commands. 
Try doing some arithmetic (or bit arithmetic :)) in the shell, and other basic things, e.g. test list slicing.
You shouldn't write long programs in the shell but its great for testing simple things without making a file.

# Problem 4
You can even interact with the system with python via the `os` and `sys` libraries. 

Try interacting with your file system from the python shell!
e.g. `os.system("ls"); os.system("cd XXX"); os.system("pwd")`

# Problem 5
Make a github account

# Problem 6
Make a github repo for your coronacoding club code.

# Problem 6.5
Make sure your coorna coding club local file system is very organized
e.g. the root directory (which should be on your desktop) has a folder for the different days, and within each of these folders you have code from the problems for those days (note: it's ok to have all the problems in a single file for each day too, in this case maybe you don't need a very complex file structure. But you could still make a subdirectory for `notes` or something. And having a directory per day could be good especially if you want to generate files like graphics and text files).

# Problem 7
Using the git cli, push your coronacodingclub stuff to your github repo

Hint: here are some useful commands

- git add .
- git commit -m "message"
- git status
- git pull origin master
- git push origin master
- git log
- git clone xxx

# Problem 7.5
Fork Alek's coronacoding github repo, make a local copy of it, make an edit (e.g. fix a typo, there are a lot of them!) and figure out how to issue a pull request, and make alek merge your pull request.

# Problem 8
If you are on a mac, run the following in your terminal:
(install `brew`, a package manager, and then install `iterm2`, a terminal replacement)
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install cask
brew cask install iterm2
```
Now use iterm2 instead of Mac's default terminal.
Because it's better.

# Problem 9
Get zsh
```sh
brew install zsh
sudo sh -c "echo $(which zsh) >> /etc/shells" && chsh -s $(which zsh)
```

You can read about zsh [here](https://ohmyz.sh/)

# Problem 10
Make a "big" project (i.e. project with multiple files) in `python`.
Import a `python` function that you write in one of the files into another file!
e.g. write a gcd computing function in one file, and then have a bunch of other number theory files that use it, e.g. a file to create the lcm(i,j) graphic on the coronacoding club homepage.

# Problem 11
Set up the subl command.
[reference website](https://ashleynolan.co.uk/blog/launching-sublime-from-the-terminal )


