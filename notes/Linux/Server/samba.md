# Samba

Samba is a file sharing service that can be ran on linux to host `smb` file structures over the network. This is useful especially in my case for connecting a share from a Linux guest machine to the Windows host. When going the other way around Virtual Box makes it very easy to for the host to share to the guest but the other way around is a little more tricky. This is also good to know for the future when wanting to set up a file share on my home network.

## Example Set Up (Ubuntu)

1) Installing Samba

```
sudo apt install samba
```

2) Configuring For Windows

After Samba is installed it should create a configuration file located in you root directory `/etc/samba/smb.conf`. There are other configuration files that samba can use though for simplicity this example is using  this one. 

Add the following to the ***global*** section to enable support for windows.

```
   wins support = yes
```

Added the network to the `interfaces` such as `interfaces = 127.0.0.0/8 192.168.56.0/24`

4) Example Shared Folder

Adding configuration for the shared folder

```
[shared_folder_name]
   path = /home/dev/Documents/GPIO_Example_2
   read only = no
   guest ok = no
   browseable = yes
   create mask = 0755
   directory mask = 0744
   valid users = dev %S
```

5) Add Shared Folder User

The samba user must be a user that already exists on the linux machine.

``` bash
sudo smbpasswd -a <user>
```

6) Restart Service

``` bash
sudo systemctl restart smbd.service
```

7) Connecting

On Windows use the following `\\<ip>\shared_folder_name` and for Linux use `smb://<ip>/shared_folder_name`.

Connect with the credentials set up with the *smbpasswd* command.
