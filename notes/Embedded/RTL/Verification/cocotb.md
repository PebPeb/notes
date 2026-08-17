# Cocotb

[Cocotb](docs.cocotb.org) is a python based testbench/verification environment for RTL.

## [Writing Testbenches](https://docs.cocotb.org/en/stable/writing_testbenches.html)

cocotb uses Python’s logging library, with the configuration described in Logging to provide some sensible defaults. cocotb.log.info is a good stand-in for print(), but user are encouraged to create their own loggers and logger hierarchy by calling logging.getLogger() and/or Logger.getChild().

``` python
import logging
import cocotb

@cocotb.test()
async def test(dut):
  # Create a logger for this testbench
  logger = logging.getLogger("my_testbench")

  logger.debug("This is a debug message")
  logger.info("This is an info message")
  logger.warning("This is a warning message")
  logger.error("This is an error message")
  logger.critical("This is a critical message")
```

Using `print()` is not recommended with cocotb ([refer to](https://docs.cocotb.org/en/stable/writing_testbenches.html)).


### [Accessing Design](https://docs.cocotb.org/en/stable/writing_testbenches.html#accessing-the-design)

When cocotb initializes it finds the toplevel instantiation in the simulator and creates a handle called dut. Toplevel signals can be accessed using the “dot” notation used for accessing object attributes in Python. The same mechanism can be used to access signals inside the design.

``` python
# Get a reference to the "clk" signal on the toplevel
clk = dut.clk

# Get a reference to a register "count"
# in a sub-block "inst_sub_block"
# (the instance name of a Verilog module or VHDL entity/component)
count = dut.inst_sub_block.count
```

## [Coroutines and Tasks](https://docs.cocotb.org/en/stable/coroutines.html)

Typically coroutines await a Trigger object which pauses the task, and indicates to the simulator some event which will cause the task to resume execution. For example:

``` python
async def wait_10ns():
  cocotb.log.info("About to wait for 10 ns")
  await Timer(10, unit='ns')
  cocotb.log.info("Simulation time has advanced by 10 ns")
```

``` python
async def wait_100ns():
  for i in range(10):
    await wait_10ns()
```

Coroutines can be scheduled for concurrent execution with start_soon(). These concurrently running coroutines are called Tasks.


