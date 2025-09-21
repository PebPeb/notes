# SSH Keys and Access

Setting up an **ssh** key can help make signing into a remote server much faster and easier. To do this both the server and client side must share a key. This key can be generated on the client side and then shared with the server with very few commands need.To start lets talk about what directories we are going to be working in. On default ssh sets up two directories to be used, one as a global use and another local one.

``` bash
~/.ssh/                 # Local Directory
/etc/ssh/               # Global Directory
```

In each directory there is a config file. The host only needs to be configured in one of these directories depending on the needs. If configured in the global directory all uses can access that host. Though if configured in the local directory only that user on the client side can access the host. For both the global and local config files follow the same configuration in the config.

``` 
Host <alias>
    HostName <IP/Domain>
    User <Username>
    IdentityFile <pathToKey>
```

The `IdentifyFile` is the private key not the public key. The public key is denoted with `.pub`, and the public key is what is shared with the server from the client.

Within the config file the *IdentityFile* tag is referring to the ssh key on the local host. If a key has already been generated then you should be able to find it in either the local or global ssh directories. If there is no key then a key will need to be generated. After the key is generated it will need to be shared with the server.

``` bash
ssh-keygen                              # Generates the key
ssh-copy-id -i <pathToKey>.pub user@host    # Copy key to server
```

After a key has been shared with the server it is as simple as using the ssh command to connect.

``` bash
ssh <alias>
```

## Manually Moving Keys

In case the case of having to manually copy the key on the server side because `ssh-copy-id` is not available. The contents of the **public** key on the client side must be copied to the `.ssh/authorized_keys` file on the server side. The `authorized_keys` file can have multiple keys copied to it, and the file can be created if it is missing from the desired ssh directory. 

Example for what it would look like to copy the public key to the authorized_keys.

``` bash
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9vP9Xt7YX+3VJXwJ5z0z4O7LtU9ZGqkR8ZtPS6nLgZFxBt7uU4X9aBqJxDLqK8GwT/YKwNgy1mFY56uFqLreVvZhYwZ1dG5Z8zyx2+S+1+Ee3tNQaZ9B6LCu+OjNUU3IxT1VpDdT6cI+avJgB8zq3GVlRxY6jGjvnImw7N0DZ5Sb3dMLkRoLVRV9FvIqzQgqZBzU6wDvnA7UMbbNdwP3vOfRzLzkHF8X example@fakemachine
```


## Generating Specific Key Types

The most common key you will probably see now a days is the `ed25519` it is a good mix of performance and security. Another common key used is the `RSA` though this key is larger therefor more secure. It requires more resources to calculate and slow down systems if resources is an issue.

``` bash
ssh-keygen                                   # default is ed25519
ssh-keygen -t ed25519 -C "my@email.com"      # 256 bits
ssh-keygent -t RSA -C "my@email.com"         # 2048, 3072, & 4096 bits
```

There are many more key types but these are the most likely to be encountered.


