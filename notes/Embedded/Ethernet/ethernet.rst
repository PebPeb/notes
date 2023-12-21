
General Ethernet Notes
----------------------


Medium Access Control (MAC)
===========================


+------+------+------+------+------+------+------+------+------+------+
| IFG  | Preamble    | SFD  | Payload                   | CRC  | IFG  |
+------+------+------+------+------+------+------+------+------+------+

**IFG** - Enforces the inter-frame gap between ethernet frames

**Preamble & SFD** - Issues the preamble and start of frame delimiter

**CRC** - Calculate/check the CRC

Physical Coding Sublayer (PCS)
==============================

The Core functionality of the PCS is as follows.

- Maintains clock synchronization when there is no data.
- Encodes data to ensure a good spread of 1's and 0's.
- Encoding transmission blocks (start of frame / end of frame)