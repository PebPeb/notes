# C

This set of notes is to help keep a simplified list of different macros and common practices in Linux. Writing kernel modules and device drivers it is easy to be bogged down with all the different libraries and macros. Hopefully I can build a list to help jog memories and make it easy to remember.

## Macros

### Linux Kernel

- *module_init\(\)* : Used to specify the initialization function that should be called when a module is loaded into the kernel
- *module_exit\(\)* : Used to specify the cleanup or exit function that should be called when a module is unloaded from the kernel
- *\_\_func\_\_* : Provides the name of the current function as a string