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

There are multiple ways to use `XSIM` stand alone. One of the easiest ways is using a project file `.prj`. The project file follows the following format.

```
verilog <work_library> <file_names>... [-d <macro>]...[-i <include_path>]... 
vhdl <work_library> <file_name>
sv <work_library> <file_name>
vhdl2008 <work_library> <file_name>
```

Example

```
verilog xil_defaultlib "mux2.v"
verilog xil_defaultlib "mux2_tb.v"
```

By default through all these stages if a specific library is not specified then `work` is used by default.

## Parsing

- **xvhdl**: Parses VHDL
- **xvlog**: Parses Verilog
- **xvlog -sv**: Parses SystemVerilog

After parsing by default this will create a simulation working file. If not specified the default work library is `work`.

``` bash
xvlog <work_library> <file_names>
xvlog xil_defaultlib mux2.v mux2_tb.v
xvlog work mux2.v mux2_tb.v
```

A simulation project file can also be used during parsing.

``` bash
xvlog -prj <file.prj>
xvlog xil_defaultlib -prj <file.prj>
xvlog work -prj <file.prj>
```

## Elaborating

- **xelab**: Elaborates a parsed design and generates a snap shot

If the working library is not specified then `work` is used by default.

``` bash
xelab <top_module>
xelab mux2_tb
xelab xil_defaultlib.mux2_tb
xelab work.mux2_tb
```

The elaboration stage can also use a project file. If a project file is used with the elaboration stage it will call the parsing stage before running, and is unnecessary to run the parsing stage.

``` bash
xelab <top_module> -prj <file.prj>
xelab mux2_tb -prj <file.prj>
xelab xil_defaultlib.mux2_tb -prj <file.prj>
xelab work.mux2_tb -prj <file.prj>
```

This stage also allows for what nets will be seen during the simulation stage. The following arguments can be added to the `xelab` command for the desired outcome.

- **-debug all**: Dumps all the nets and slower to simulate
- **-debug typical**: Dumps a reduced number of nets and faster to simulate

**Note** `-debug` is critical for generating waveforms.

## Simulation

- **xsim**

``` bash
xsim <elaborated_design>
xsim mux2_tb
xsim xil_defaultlib.mux2_tb
xsim work.mux2_tb
```

Running `xsim` without any arguments just opens up a command line interface. The following arguments can be used to more streamline the use of the command.

- **-R**: Runs the entire simulation through
- **-gui**: Opens simulation in Vivado's graphical interface

