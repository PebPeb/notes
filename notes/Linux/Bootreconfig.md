




## Rebuild building bootloader

The `--bootloader-id=ubuntu` would write or overwrite bootloader located in `/boot/efi/EFI/ubuntu`. To create a new bootloader replace `ubuntu` in `--bootloader-id=` with desired name. This is so the same with were ever the efi boot is located `--efi-directory=/boot/efi`.

``` bash
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=ubuntu --recheck
update-grub
```

## Boot Broken

If boot is broken possible solution for repairing is  by following. Live boot using a USB stick. From the terminal in the live boot do the following.

Mount the necessary drives. If root and boot are on different partitions you will have to correctly configure the file system.


``` bash
sudo mount /dev/<root_drive> /mnt
sudo mount /dev/<efi_boot_drive> /mnt/boot/efi
```

For the next steps we need to configure the mounted root directory in preparation for changing the root. These virtual filesystems are key for the kernel to operate.

``` bash
sudo mount --bind /dev /mnt/dev 
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys
```

Not always needed but have run into issues without it.

``` bash
sudo mount --bind /run /mnt/run
```

Change root

``` bash
sudo chroot /mnt
```

From here following the steps outlined it [Rebuild building bootloader](#rebuild-building-bootloader) will reconfigure the bootloader.
