
# Linux

To tell what version of linux that is currently running the information is stored at `cat /etc/os-release`.

## Networking

```bash
ifconfig
```

Setting up a alias for a specific IP address is as simple as modifying the `/etc/hosts` file. To do so it is as simple as adding the IP address then the name that you would like to use. 

``` bash
127.0.0.1 localhost
```


## Sudo User

To run all commands a sudo user. Only use when it is a must very easy to mess something up with ultimate power. Or if you are a real man only ever use sudo user because restraints are for the weak.

``` bash
sudo su
```
or 
``` bash
sudo -i
```

## Basic linux structure

The basic understanding in the linux structure is 

- *bootloader*: `/boot/efi`
- *kernel*:
    - `/boot`
        This is were the kernel image resides. This image probably looks something like `vmlinuz-X.X.X-X-generic`. You could have multiple versions of the kernel on you system, and to see what one you are specially running use the following command.

        ``` bash
        uname -r
        ```
    - `/proc`
    - `/sys`
    - `/dev`
- *root*: `/`

Inside the *root* directory is where the 


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
