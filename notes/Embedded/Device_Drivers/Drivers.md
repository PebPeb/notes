
# Device Driver Basics

Understand Kernel Modules first

``` bash
$ ls -l /dev/hda[1-3]
brw-rw----  1 root  disk  3, 1 Jul  5  2000 /dev/hda1
brw-rw----  1 root  disk  3, 2 Jul  5  2000 /dev/hda2
brw-rw----  1 root  disk  3, 3 Jul  5  2000 /dev/hda3
```

Notice the column of numbers separated by a comma. The first number is called the device’s major number. The second number is the minor number. The major number tells you which driver is used to access the hardware. Each driver is assigned a unique major number; all device files with the same major number are controlled by the same driver. All the above major numbers are 3, because they’re all controlled by the same driver.

The minor number is used by the driver to distinguish between the various hardware it controls. Returning to the example above, although all three devices are handled by the same driver they have unique minor numbers because the driver sees them as being different pieces of hardware.

## File Operations

The file_operations structure is defined in include/linux/fs.h, and holds pointers to functions defined by the driver that perform various operations on the device. Each field of the structure corresponds to the address of some function defined by the driver to handle a requested operation.



## Character devices and Block devices

The difference is that block devices have a buffer for requests, so they can choose the best order in which to respond to the requests.

<!-- ``` bash
mknod
``` -->

## Registering A Device

Char devices are accessed through device files, usually located in /dev. Adding a driver to your system means registering it with the kernel. This is synonymous with assigning it a major number during the module’s initialization. You do this by using the *register_chrdev* function, defined by *include/linux/fs.h*.

  ``` C
    int register_chrdev(unsigned int major, const char *name, struct file_operations *fops);
  ```

  In this function the unsigned int major is the major number you want to request, *const char \*name* is the name of the device as it will appear in /proc/devices and *struct file_operations \*fops* is a pointer to the *file_operations* table for the driver. Note that we didn’t pass the minor number to *register_chrdev* . That is because the kernel doesn’t care about the minor number; only the driver uses it.

  To avoid hijacking a reserved major number by the kernel the kernel can assign one dynamically. Passing in **0** as the major number will result in the kernel dynamically allocating a major number to driver.

## Talking to Device Files

*device write*
*ioctl* Input Output Control



