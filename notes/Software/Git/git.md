
# Git Commands

Quick cheat sheet for working with git.

## Cloning New Repo

Git can use either **HTTPS** or **SSH** for cloning and working with repos. Just like any SSH client a key will need to be set up in order to be used with SSH. Refer to the notes on SSH key generation for further details.

``` bash
git clone <repo>
```

To clone a specific branch the following command can be used.

``` bash
git clone -b <branch-name> <repo>
```

## Working With Git

...

``` bash
git checkout <branch-name>

git branch                                 # Display Local branches                                 
git fetch                                  # Gits all the changes from the repo/branches
```
...

## Changing Git Configurations

Some times it is necessary to change the default git configurations. This can be set for the specific project or a default for all git projects.

``` bash
git config <configuration> <new-value>             # Current Project
git config --system <configuration> <new-value>    # System Configs for users
git config --global <configuration> <new-value>    # Global Configs
```
To see the current configurations the following command can be used.

``` bash
git config -l 
```

Typically the most useful configurations are the `user.name` and `user.email`. These two together are what is used to determine who is making the changes. So when git hub is displaying who made the changes it is because of these configurations. Below is an example of how you might change them for a specific project.

``` bash
git config user.name "John Doe"
git config user.email "JohnDoe@email.com"
```