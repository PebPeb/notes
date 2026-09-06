# Cocotb Clocks

## Creating a simple Clock


``` python
import cocotb
from cocotb.clock import Clock
...
@cocotb.test()
async def my_test(dut):
  ...
  clock = Clock(dut.clk, 10, units="ns")
  cocotb.start_soon(clock.start())
  ...
```