

``` bash
ssh-keygen -R <ip>  # Removing host from known_hosts
```


## Kernel

To see the current version of the kernel on your system 

``` bash
uname -r
```

## Working with Disks & Partitions

To list drives and partitions use the following. After listing the partitions `fdisk` can be used to work with disk. Use `m` to list help with `fdisk`.

``` bash
lsblk
sudo fdisk /dev/<partition>
```
