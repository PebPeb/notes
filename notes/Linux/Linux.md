
# Linux

To tell what version of linux that is currently running the information is stored at `cat /etc/os-release`.

## SSH Helpful Commands

``` bash
ssh-keygen -R <ip>  # Removing host from known_hosts
```

## New Users

``` bash
sudo adduser <new_user>
sudo adduser --shell /bin/false <new_user>      # Without shell access 
sudo deluser <user>
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

After reading the outputs of the `lsblk` to un-mount a drive you can use the following command.

``` bash
umount /dev/<partition>
```

To example for reformating disks.

``` bash
sudo mkfs.vfat -F 32 /dev/<partition>   # FAT32
```


## Miscellaneous Commands

### Neofetch

Fancy way of returning system information

``` bash
neofetch
```

### btop

A more fancy top

``` bash
btop
```
