# Tcl commands for Simulation Filesets


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


# Simulating with XSIM

There are multiple ways to use `XSIM` stand alone.

## Parsing

- **xvhdl**: Parses VHDL
- **xvlog**: Parses Verilog
- **xvlog -sv**: Parses SystemVerilog

After parsing by default this will create a simulation working file. 