
# Platform Drivers


``` C
static struct platform_driver mypdrv = { 
    .probe    = my_pdrv_probe, 
    .remove   = my_pdrv_remove, 
    .driver   = { 
        .name     = "my_platform_driver", 
        .owner    = THIS_MODULE, 
    }, 
}; 
```

- `probe()` : Is the function that gets called when a device claims your driver after a match occurs. 

``` C
static int my_pdrv_probe(struct platform_device *pdev) 
```

- `remove()` : This is called to get rid of the driver when it is not needed anymore by devices.

``` C
static int my_pdrv_remove(struct platform_device *pdev) 
```