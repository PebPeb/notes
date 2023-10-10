
# Kernel Modules

Kernel Object file or `.ko`. Allows for the dynamically adding and removing of functionality without having to recompile the entire kernel. 

``` bash
insmod
modprobe
rmmod
lsmod
modinfo <.ko>              # Sees the info of the module
```

That gives you details about what system calls a program is making
``` bash
strace ./<compiled_program>
```

## Reading Kernel Outputs

``` bash
dmesg
cat /var/log/kern.log
```

