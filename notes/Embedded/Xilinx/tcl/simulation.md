# Tcl commands for Simulation


```tcl
create_fileset -simset <name>
```

In the case of not wanting to include a source set (this is all the files from a specific source).

##

```tcl
set_property SOURCE_SET {} [get_filesets <name>]
```

## Launching simulation


## Updating file set

update_compile_order -fileset <name>