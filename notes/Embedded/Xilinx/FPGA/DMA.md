
# AXI DMA (Direct Memory Access)

[Kernel DMA-API](https://www.kernel.org/doc/Documentation/DMA-API.txt)

MM2S - Memory-mapped to Stream
  Transports data from DDR memory to FPGA.

S2MM - Stream to Memory-mapped
  Transports arbitrary dat stream to DDR memory.


## Register Address Map


| Offset | Name | Description |
|--------|------|-------------|
| 0x18   | MM2S_SA         | MM2S Source Address. Lower 32 bits of address. |
| 0x1C   | MM2S_SA_MSB     | MM2S Source Address. Upper 32 bits of address. |
| 0x48   | S2MM_DA         | S2MM Destination Address. Lower 32 bit address. |
| 0x4C   | S2MM_DA_MSB     | S2MM Destination Address. Upper 32 bit address. |
| 0x58   | S2MM_LENGTH     | S2MM Buffer Length (Bytes) |