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

Within the config file the *IdentityFile* tag is referring to the ssh key on the local host. If a key has already been generated then you should be able to find it in either the local or global ssh directories. If there is no key then a key will need to be generated. After the key is generated it will need to be shared with the server.

``` bash
ssh-keygen                              # Generates the key
ssh-copy-id -i <pathToKey> user@host    # Copy key to server
```

After a key has been shared with the server it is as simple as using the ssh command to 
connect.

``` bash
ssh <alias>
```

## Generating Specific Key Types

The most common key you will probably see now a days is the `ed25519` it is a good mix of performance and security. Another common key used is the `RSA` though this key is larger therefor more secure. It requires more resources to calculate and slow down systems if resources is an issue.

``` bash
ssh-keygen                                   # default is ed25519
ssh-keygen -t ed25519 -C "my@email.com"      # 256 bits
ssh-keygent -t RSA -C "my@email.com"         # 2048, 3072, & 4096 bits
```

There are many more key types but these are the most likely to be encountered.
